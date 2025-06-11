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

    :param : url to search for ollama
    :rtype: str
    :return: boolean
    :rtype: bool
    """
    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Start of function is_ollama_running, ollama_url to check = %s', str(ollama_url))

    try:
        requests.get(ollama_url)
        logger.info('Ollama is running, end of function is_ollama_running')
        return True
    except requests.exceptions.ConnectionError as e:
        logger.error('Program exit on exception EXT-000009 = %s', str(e))
        sys.exit()
