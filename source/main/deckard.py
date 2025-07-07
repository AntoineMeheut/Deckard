# -*- coding: utf-8 -*-

import sys
import json
import argparse
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from source.modules.functions.run_tests import run_tests
from source.modules.functions.run_replay import run_replay
from source.modules.functions.validate_api_keys import validate_api_keys
from source.modules.functions.validate_ollama_model import validate_ollama_model
from source.modules.utils.show_help import show_help
from source.modules.utils.logger import setup_logging

__all__ = ['main']


def main():
    """
    | Deckard program is a tool for asking humorous questions and playing with replicants.
    |
    | This program works in two distinct steps. The first step allows you to test prompts in an LLM and obtain
    | a json file with all the tested prompts and the responses given by the LLM. This step allows you to check
    | which prompts have an effect on the LLM and which ones do not pass due to the protections that exist in the LLM.
    | The json file will then allow you to prepare the second step. You just need to insert the response of the prompt
    | that worked, in your input yaml file and then you can replay the attacks at any time.
    |
    | To tell the program which step you want to run, simply use the --step parameter, specifying the values 1 or 2.
    |
    | The prompts are located in the "voight-kampff" directory, you can add your own prompts there,
    | respecting the yaml file format.
    |
    | Exception management :
    | If IOError or any exception : log the trace of the exception stack and stop the execution of the programme.

    Usage Examples:
    ---------------
    1. Test with OpenAI:
        python deckard.py --step 1 --model gpt-3.5-turbo --model-type openai

    2. Test with Anthropic:
        python deckard.py --step 1 --model claude-3-opus-20240229 --model-type anthropic

    3. Test with Ollama:
        python deckard.py --step 1 --severity high --model mistral --model-type ollama --prompts ../../resource/system-prompts/system-prompts-normal.txt

    4. Run specific rules:
        python deckard.py --step 1 --model gpt-4 --model-type openai --rules prompt_stealer,distraction_basic

    5. Custom options:
        python deckard.py --step 1 --model gpt-4 --model-type openai --iterations 3 --output results_gpt4.json

    6. Firewall testing mode:
        python deckard.py --step 1 --model gpt-4 --model-type openai --firewall --pass-condition="true"
        # In firewall mode, tests pass only if the response contains the specified string
        # and is not more than twice its length

    Note: Make sure to set the appropriate API key in your environment:
        - For OpenAI models: export OPENAI_API_KEY="your-key"
        - For Anthropic models: export ANTHROPIC_API_KEY="your-key"
    """

    logging = setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Main program: starting to initialize the appropriate client based on the model type....')

    print(r'''
________                 __                     .___              
\______ \   ____   ____ |  | _______ _______  __| _/              
 |    |  \_/ __ \_/ ___\|  |/ /\__  \\_  __ \/ __ |               
 |    `   \  ___/\  \___|    <  / __ \|  | \/ /_/ |               
/_______  /\___  >\___  >__|_ \(____  /__|  \____ |               
        \/     \/     \/     \/     \/           \/       
Replicants prompts injection tests !
    ''')
    parser = argparse.ArgumentParser(description="Test LLM system prompts against injection attacks")
    parser.add_argument("--prompts", default="../../resource/system-prompts/system-prompts-normal.txt", help="Path to system prompts file")
    parser.add_argument("--step", required=True, help="Type of cycle to do")
    parser.add_argument("--model", required=True, help="LLM model name")
    parser.add_argument("--model-type", required=True, choices=["openai", "anthropic", "ollama"],
                        help="Type of the model (openai, anthropic, ollama)")
    parser.add_argument("--severity", type=lambda s: [item.strip() for item in s.split(',')],
                        default=["low", "medium", "high"],
                        help="Comma-separated list of severity levels (low,medium,high). Defaults to all severities.")
    parser.add_argument("--rules", type=lambda s: [item.strip() for item in s.split(',')],
                        help="Comma-separated list of rule names to run. If not specified, all rules will be run.")
    parser.add_argument("--output", default="results.json", help="Output file for results")
    parser.add_argument("-y", "--yes", action="store_true", help="Automatically answer yes to all prompts")
    parser.add_argument("--iterations", type=int, default=1, help="Number of iterations to run for each test")
    parser.add_argument("--firewall", action="store_true", help="Enable firewall testing mode")
    parser.add_argument("--pass-condition", help="Expected response in firewall mode (required if --firewall is used)")

    try:
        args = parser.parse_args()
        
        # Validate severity levels
        valid_severities = {"low", "medium", "high"}
        if args.severity:
            invalid_severities = [s for s in args.severity if s not in valid_severities]
            if invalid_severities:
                raise ValueError(f"Invalid severity level(s): {', '.join(invalid_severities)}. Valid levels are: low, medium, high")
        
        # Validate firewall mode arguments
        if args.firewall and not args.pass_condition:
            raise ValueError("--pass-condition is required when using --firewall mode")
        
        # Validate model before running tests
        common_paths = [
            "/usr/local/bin/ollama",  # Default macOS install location
            "/opt/homebrew/bin/ollama",  # M1 Mac Homebrew location
            "ollama"  # If it's in PATH
        ]
        ollama_url = "http://localhost:11434"
        ollama_models_url = "http://localhost:11434/api/tags"

        if not validate_ollama_model(args.model, args.model_type, common_paths, ollama_url, ollama_models_url, args.yes):
            return 1
        
        print("\nTest started...")

        if not validate_api_keys(args.model_type):
            logger.error('Main program: no KEY environment variable found, it is required')
            sys.exit()

        if args.step == "1":
            results = run_tests(args.model, args.model_type, args.prompts, common_paths, ollama_url, args.iterations,
                              args.severity, args.rules, args.firewall, args.pass_condition)
        elif args.step == "2":
            results = run_replay(args.model, args.model_type, args.prompts, common_paths, ollama_url, args.iterations,
                                args.severity, args.rules, args.firewall, args.pass_condition)
        else:
            logger.error('Main program: error step = %s', str(args.step))
            show_help()
            return 1

        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
            
    except ValueError as e:
        logger.error('Main program: error %s', str(e))
        show_help()
        return 1
    except Exception as e:
        logger.error('Main program: error %s', str(e))
        show_help()
        return 1
        
    return 0


if __name__ == "__main__":
    """
    Execute a sys.exit and call the main program giving it the arguments passed to the program at the time of execution
    """

    sys.exit(main()) # pragma: no cover
