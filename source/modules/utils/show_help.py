#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import source.modules.utils.logger as utils

__all__ = ['show_help']

def show_help():
    """
    Show help message with usage examples.

    Function input: none

    Function output: none

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme.

    The program stops with a log with the exit code EXT-000017.

    """

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Start of function show_help')

    try:
        print("""
            Usage Examples:
            -------------
            1. Test with OpenAI:
                python deckard.py --step 1 --model gpt-3.5-turbo --model-type openai --prompts ../../resource/system-prompts/system-prompts-normal.txt

            2. Test with Anthropic:
                python deckard.py --step 1 --model claude-3-opus-20240229 --model-type anthropic --prompts ../../resource/system-prompts/system-prompts-normal.txt

            3. Test with Ollama:
                python deckard.py --step 1 --model mistral --model-type ollama --prompts ../../resource/system-prompts/system-prompts-normal.txt

            4. Run specific rules:
                python deckard.py --step 1 --model gpt-4 --model-type openai --rules prompt_stealer,distraction_basic --prompts ../../resource/system-prompts/system-prompts-normal.txt

            5. Custom options:
                python deckard.py --step 1 --model gpt-4 --model-type openai --iterations 3 --output results_gpt4.json --prompts ../../resource/system-prompts/system-prompts-normal.txt

            6. Firewall testing mode:
                python deckard.py --step 1 --model gpt-4 --model-type openai --firewall --pass-condition="true" --prompts ../../resource/system-prompts/system-prompts-normal.txt
                # In firewall mode, tests pass only if the response contains the specified string
                # and is not more than twice its length

            Note: Make sure to set the appropriate API key in your environment:
                - For OpenAI models: export OPENAI_API_KEY="your-key"
                - For Anthropic models: export ANTHROPIC_API_KEY="your-key"
            """)
    except Exception as e:
        logger.error('Program exit on exception EXT-000017 = %s', str(e))
        sys.exit()