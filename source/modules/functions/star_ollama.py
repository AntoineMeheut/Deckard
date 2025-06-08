# -*- coding: utf-8 -*-
import subprocess
import time
import requests

import source.modules.utils.logger as utils
from source.modules.functions.get_ollama_path import get_ollama_path
from source.modules.functions.is_ollama_running import is_ollama_running

__all__ = ['start_ollama']


def start_ollama(common_paths, ollama_url):
    """
    Start Ollama server.

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme

    :param : common_paths
    :rtype: str
    :return: boolean
    :rtype: bool
    """

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Starting Ollama server...')

    try:
        ollama_path = get_ollama_path(common_paths)
        subprocess.Popen([ollama_path, "serve"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Wait for server to start
        for _ in range(10):
            if is_ollama_running(ollama_url):
                logger.info('Ollama server is running')
                return True
            time.sleep(1)
        return False
    except FileNotFoundError as e:
        logger.error('Exception = %s', str(e))
        return False
