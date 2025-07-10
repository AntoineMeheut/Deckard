# -*- coding: utf-8 -*-
import os
import sys
import source.modules.utils.logger as utils

__all__ = ['get_ollama_path']


def get_ollama_path(common_paths):
    """
    Get the path to ollama executable

    Function input: list of common path for ollama software

    Function output: the path of the ollama software

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme.

    The program stops with a log with the exit code EXT-000006.

    :param: common_paths is the ollama computer path, like : /usr/local/bin/ollama or /opt/homebrew/bin/ollama or ollama
    :ptype: list
    :return: path is the ollama computer path, like : /usr/local/bin/ollama on macbook
    :rtype: str
    """
    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Function get_ollama_path: start to get the path to ollama executable')

    try:
        for path in common_paths:
            if os.path.exists(path):
                logger.info('Function get_ollama_path: end of function get_ollama_path, ollama path is = %s', str(path))
                return path
            elif os.system(f"which {path} > /dev/null 2>&1") == 0:
                logger.info('Function get_ollama_path: end of function get_ollama_path, ollama path is = %s', str(path))
                return path
            else:
                logger.error('Function get_ollama_path: EXT-000006-1-ollama executable not found. Please make sure Ollama is installed.')
                sys.exit()
        return None
    except Exception as e:
        logger.error('Function get_ollama_path: EXT-000006-2-exit on exception = %s', str(e))
        sys.exit()
