# -*- coding: utf-8 -*-
import sys
import subprocess
import time
import source.modules.utils.logger as utils
from source.modules.functions.get_ollama_path import get_ollama_path
from source.modules.functions.is_ollama_running import is_ollama_running

__all__ = ['start_ollama']


def start_ollama(common_paths, ollama_url):
    """
    Start Ollama server.

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme.

    The program stops with a log with the exit code EXT-000014.

    :param: common_paths is the ollama computer path, like : /usr/local/bin/ollama or /opt/homebrew/bin/ollama or ollama
    :ptype: list
    :return: boolean, return True if ollama is running
    :rtype: bool
    """

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Function start_ollama: starting Ollama server...')

    try:
        ollama_path = get_ollama_path(common_paths)
        subprocess.Popen([ollama_path, "serve"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Wait for server to start
        for _ in range(10):
            if is_ollama_running(ollama_url):
                logger.info('Function start_ollama: Ollama server is running')
                return True
            time.sleep(1)
        return False
    except FileNotFoundError as e:
        logger.error('Function start_ollama: exit on exception EXT-000014 = %s', str(e))
        sys.exit()
