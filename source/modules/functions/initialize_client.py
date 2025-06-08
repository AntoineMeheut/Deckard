# -*- coding: utf-8 -*-
import os
import sys

from openai import OpenAI
import anthropic
import source.modules.utils.logger as utils

from source.modules.functions.star_ollama import start_ollama
from source.modules.functions.is_ollama_running import is_ollama_running

__all__ = ['initialize_client']


def initialize_client(model_type: str, common_paths: list, ollama_url: str):
    """
    Initialize the appropriate client based on the model type.

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme

    :param : model_type
    :rtype: str
    :return: none
    :rtype: none
    """

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Starting to initialize the appropriate client based on the model type....')

    try:
        if model_type == "openai":
            return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        elif model_type == "anthropic":
            return anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        elif model_type == "ollama":
            if not is_ollama_running(ollama_url):
                if not start_ollama(common_paths, ollama_url):
                    logger.error('Failed to start Ollama server')
            sys.exit()
        else:
            logger.error('Unsupported model type: %s', str(model_type))
            sys.exit()
    except Exception as e:
        logger.error('Exception = %s', str(e))
        sys.exit()
