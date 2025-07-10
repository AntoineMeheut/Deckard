# -*- coding: utf-8 -*-
import os
import sys
import anthropic
from openai import OpenAI
import source.modules.utils.logger as utils

from source.modules.functions.start_ollama import start_ollama
from source.modules.functions.is_ollama_running import is_ollama_running

__all__ = ['initialize_client']


def initialize_client(model_type: str, common_paths: list, ollama_url: str):
    """
    Initialize the appropriate client based on the model type.

    Function input: the AI model to use (OpenAI, Anthropic ou Ollama model), the ollama software common path list, the ollama server url

    Function output: openai_key or anthropic_key or True if ollama model is downloaded and started

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme.

    The program stops with a log with the exit code EXT-000008.

    :param: model_type like ollama or openai or anthropic
    :ptype: str
    :param: common_paths is the ollama computer path, like : /usr/local/bin/ollama or /opt/homebrew/bin/ollama or ollama
    :ptype: list
    :param: ollama_models_url, local url for ollama model, like http://localhost:11434/api/tags
    :ptype: str
    :return: none
    :rtype: none
    """

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Function initialize_client: starting to initialize the appropriate client based on the model type....')

    try:
        if model_type == "openai":
            try:
                openai_key = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
                return openai_key
            except Exception as e:
                logger.error('Function initialize_client: EXT-000008-1-exception on reading openai_key = %s', str(e))
                return "False"
        elif model_type == "anthropic":
            try:
                anthropic_key = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
                return anthropic_key
            except Exception as e:
                logger.error('Function initialize_client: EXT-000008-2-exception on reading anthropic_key = %s', str(e))
                return "False"
        elif model_type == "ollama":
            try:
                if not is_ollama_running(ollama_url):
                    if not start_ollama(common_paths, ollama_url):
                        logger.error('Function initialize_client: EXT-000008-3-failed to start Ollama server')
                        return "False"
                    return "True"
                return "True"
            except Exception as e:
                logger.error('Function initialize_client: EXT-000008-4-exception on starting ollama = %s', str(e))
                return "False"
        else:
            logger.error('Function initialize_client: EXT-000008-5-unsupported model type: %s', str(model_type))
            return "False"
    except Exception as e:
        logger.error('Function initialize_client: EXT-000008-6-exit on exception= %s', str(e))
        sys.exit()
