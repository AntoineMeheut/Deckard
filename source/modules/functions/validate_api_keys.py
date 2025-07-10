# -*- coding: utf-8 -*-
import sys
import os
import source.modules.utils.logger as utils

__all__ = ['validate_api_keys']


def validate_api_keys(model_type: str):
    """
    Validate that required API keys are present for openai or anthropic.

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme.

    The program stops with a log with the exit code EXT-000016.

    :param: common_paths is the ollama computer path, like : /usr/local/bin/ollama or /opt/homebrew/bin/ollama or ollama
    :ptype: list
    :return: bool is ollama is running
    :rtype: boolean
    """

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Function validate_api_keys: starting to validate that required API keys are present for openai or anthropic....')

    try:
        if model_type == "openai" and not os.getenv("OPENAI_API_KEY"):
            logger.error('Function validate_api_keys: no OPENAI_API_KEY environment variable found, it is required for OpenAI models')
        elif model_type == "anthropic" and not os.getenv("ANTHROPIC_API_KEY"):
            logger.error('Function validate_api_keys: no ANTHROPIC_API_KEY environment variable found, it is required for Anthropic models')
        elif "ollama" == model_type:
            logger.info("Function validate_api_keys: Ollama model no key needed")
            return True
        return False
    except Exception as e:
        logger.error('Function validate_api_keys: exit on exception EXT-000016 = %s', str(e))
        sys.exit()
