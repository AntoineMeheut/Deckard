# -*- coding: utf-8 -*-
import os
import sys
import source.modules.utils.logger as utils

__all__ = ['validate_api_keys']


def validate_api_keys(model_type: str):
    """
    Validate that required API keys are present for openai or anthropic.

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme

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
        return False
    except Exception as e:
        logger.error('Exception = %s', str(e))
        return False
