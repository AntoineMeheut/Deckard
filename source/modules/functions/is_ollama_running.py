# -*- coding: utf-8 -*-
import sys
import requests
import source.modules.utils.logger as utils

__all__ = ['is_ollama_running']

def is_ollama_running(ollama_url) -> bool:
    """
    Check if Ollama server is running.

    Function input: the ollama server url

    Function output: True if ollama server is running

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme.

    The program stops with a log with the exit code EXT-000009.

    :param: ollama_models_url, local url for ollama model, like http://localhost:11434/api/tags
    :ptype: str
    :param: boolean response is False or True if model running
    :type: bool
    """
    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Function is_ollama_running: start of function, ollama_url to check = %s', str(ollama_url))

    try:
        requests.get(ollama_url)
        logger.info('Function is_ollama_running: Ollama is running')
        return True
    except requests.exceptions.ConnectionError as e:
        logger.error('Function is_ollama_running: exit on exception EXT-000009 = %s', str(e))
        sys.exit()
