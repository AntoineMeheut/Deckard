# -*- coding: utf-8 -*-
import sys
import os
import source.modules.utils.logger as utils

__all__ = ['validate_api_keys']


def validate_api_keys(model_type: str):
    """
    Validate that required API keys are present for openai or anthropic.

    Function input: model_type (could be OpenAI or Anthropic)

    Function output: False if API KEY is not present

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme.

    The program stops with a log with the exit code EXT-000016.

    :param : model_type
    :rtype: str
    :return: none
    :rtype: none
    """

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Starting to validate that required API keys are present for openai or anthropic....')

    try:
        if model_type == "openai" and not os.getenv("OPENAI_API_KEY"):
            logger.error('No OPENAI_API_KEY environment variable found, it is required for OpenAI models')
        elif model_type == "anthropic" and not os.getenv("ANTHROPIC_API_KEY"):
            logger.error('No ANTHROPIC_API_KEY environment variable found, it is required for Anthropic models')
        elif "ollama" == model_type:
            logger.info("Ollama model no key needed")
            return True
        return False
    except Exception as e:
        logger.error('Program exit on exception EXT-000016 = %s', str(e))
        sys.exit()
