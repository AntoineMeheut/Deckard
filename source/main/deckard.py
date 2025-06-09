import argparse
import json
import sys
from typing import Dict
import source.modules.utils.logger as utils
from source.modules.functions.initialize_client import initialize_client
from source.modules.functions.load_system_prompts import load_system_prompts

from source.modules.functions.load_test_rules import load_test_rules
from source.modules.functions.validate_api_keys import validate_api_keys
from source.modules.functions.validate_ollama_model import validate_ollama_model





def run_single_test(client, model: str, model_type: str, system_prompt: str, 
                   test_name: str, rule: dict, num_runs: int = 5,
                   firewall_mode: bool = False, pass_condition: str = None) -> Dict:
    """Run a single test multiple times and evaluate results."""
    # ANSI color codes
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    failed_result = None
    passed_count = 0
    
    print(f"  Running up to {num_runs} iterations...")
    
    for i in range(num_runs):
        response, is_error = test_prompt(client, model, model_type, system_prompt, rule['prompt'])
        passed, reason = evaluate_test_result(test_name, rule, response, is_error, system_prompt, firewall_mode, pass_condition)
        
        if passed:
            passed_count += 1
            print(f"    Iteration {i+1}: {GREEN}PASS{RESET}")
        else:
            failed_result = {
                "response": response,
                "reason": reason
            }
            if reason.startswith("API Error:"):
                print(f"    Iteration {i+1}: {YELLOW}ERROR{RESET} - {reason}")
            else:
                print(f"    Iteration {i+1}: {RED}FAIL{RESET} - {reason}")
            break  # Stop iterations on first failure
        
    overall_passed = passed_count == num_runs
    actual_runs = i + 1  # Number of actual iterations run
    
    result = {
        "type": rule['type'],
        "severity": rule['severity'],
        "passed": overall_passed,
        "pass_rate": f"{passed_count}/{actual_runs}"
    }
    
    # Only include failed result if there was a failure
    if failed_result:
        result["failed_result"] = failed_result
        
    return result

def run_tests(model: str, model_type: str, system_prompts_path: str, common_paths: list, ollama_url: str, iterations: int = 5, severities: list = None, rule_names: list = None, firewall_mode: bool = False, pass_condition: str = None) -> Dict[str, dict]:
    """Run all tests and return results."""
    # ANSI color codes
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Starting to initialize the appropriate client based on the model type....')

    print("\nTest started...")
    if not validate_api_keys(model_type):
        logger.error('No KEY environment variable found, it is required')
        sys.exit()
    client = initialize_client(model_type, common_paths, ollama_url)
    if client == "False":
        logger.error('No openai, anthropic or ollama client running, it is required')
        sys.exit()
    system_prompt = load_system_prompts(system_prompts_path)
    if system_prompt == "False":
        logger.error('no prompts file found, it is required')
        sys.exit()
    results = {}
    
    if firewall_mode and not pass_condition:
        raise ValueError("Pass condition must be specified when using firewall mode")
    
    test_rules = load_test_rules(0,0)
    
    # Filter rules based on severity and rule names
    filtered_rules = {}
    for test_name, rule in test_rules.items():
        # Check if rule matches both severity and name filters (if any)
        severity_match = not severities or rule['severity'] in severities
        name_match = not rule_names or test_name in rule_names
        
        if severity_match and name_match:
            filtered_rules[test_name] = rule
    
    if rule_names and len(filtered_rules) < len(rule_names):
        # Find which requested rules don't exist
        missing_rules = set(rule_names) - set(filtered_rules.keys())
        print(f"\n{YELLOW}Warning: The following requested rules were not found: {', '.join(missing_rules)}{RESET}")
    
    total_filtered = len(filtered_rules)
    if total_filtered == 0:
        print(f"\n{YELLOW}Warning: No rules matched the specified criteria{RESET}")
        return results
        
    for i, (test_name, rule) in enumerate(filtered_rules.items(), 1):
        print(f"\nRunning test [{i}/{total_filtered}]: {test_name} ({rule['type']}, severity: {rule['severity']})")
        result = run_single_test(client, model, model_type, system_prompt, test_name, rule, iterations, firewall_mode, pass_condition)
        
        # Print summary
        if result["passed"]:
            print(f"  Final Result: {GREEN}PASS{RESET} ({result['pass_rate']} passed)")
        else:
            if result.get("failed_result", {}).get("reason", "").startswith("API Error:"):
                print(f"  Final Result: {YELLOW}ERROR{RESET} ({result['pass_rate']} passed)")
                # Stop testing if we get an API error
                print("\nStopping tests due to API error.")
                results[test_name] = result
                return results
            else:
                print(f"  Final Result: {RED}FAIL{RESET} ({result['pass_rate']} passed)")
        
        results[test_name] = result
        
    print("\nAll tests completed.")
    return results


def main():
    """
    Deckard program is a quick attack injection tool for playing with replicants.
    The prompts are located in the "voight-kampff" directory, you can add your own prompts there,
    respecting the yaml file format.

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme

    Usage Examples:
    -------------
    1. Test with OpenAI:
        python deckard.py --model gpt-3.5-turbo --model-type openai

    2. Test with Anthropic:
        python deckard.py --model claude-3-opus-20240229 --model-type anthropic

    3. Test with Ollama:
        python deckard.py --model llama2 --model-type ollama

    4. Run specific rules:
        python deckard.py --model gpt-4 --model-type openai --rules prompt_stealer,distraction_basic

    5. Custom options:
        python deckard.py --model gpt-4 --model-type openai --iterations 3 --output results_gpt4.json

    6. Firewall testing mode:
        python deckard.py --model gpt-4 --model-type openai --firewall --pass-condition="true"
        # In firewall mode, tests pass only if the response contains the specified string
        # and is not more than twice its length

    Note: Make sure to set the appropriate API key in your environment:
        - For OpenAI models: export OPENAI_API_KEY="your-key"
        - For Anthropic models: export ANTHROPIC_API_KEY="your-key"
    """

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Starting to initialize the appropriate client based on the model type....')

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
    parser.add_argument("--prompts", default="system-prompts.txt", help="Path to system prompts file")
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
    parser.add_argument("--iterations", type=int, default=5, help="Number of iterations to run for each test")
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
            logger.error('No KEY environment variable found, it is required')
            sys.exit()

        common_paths = [
            "/usr/local/bin/ollama",  # Default macOS install location
            "/opt/homebrew/bin/ollama",  # M1 Mac Homebrew location
            "ollama"  # If it's in PATH
        ]
        ollama_url = "http://localhost:11434"

        results = run_tests(args.model, args.model_type, args.prompts, common_paths, ollama_url, args.iterations,
                          args.severity, args.rules, args.firewall, args.pass_condition)
        
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
            
    except ValueError as e:
        print(f"\n{RED}Error:{RESET} {str(e)}")
        show_help()
        return 1
    except Exception as e:
        print(f"\n{RED}Error:{RESET} An unexpected error occurred: {str(e)}")
        show_help()
        return 1
        
    return 0

if __name__ == "__main__":
    main()
