#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import source.modules.utils.logger as utils

__all__ = ['show_help']

def show_help():
    """
    Show help message with usage examples.

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
    logger.info('Start of function show_help')

    try:
        print("""
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
            """)
    except Exception as e:
        logger.error('Exception : problem during show_help = %s', str(e))
        sys.exit()