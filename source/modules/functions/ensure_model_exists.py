# -*- coding: utf-8 -*-
import sys
import ollama

import source.modules.utils.logger as utils

__all__ = ['ensure_model_exists']


def ensure_model_exists(model: str):
    """
    Ensure the Ollama model exists, download if not.
    Function input: the ollama model that we want to use
    Function output: True il the model exist, exit if not

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme.
    The program stops with a log with the exit code EXT-000003.

    :param : model
    :rtype: str
    :return: none
    :rtype: none
    """

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Check if ollama model exist...')

    try:
        ollama.list(model)
    except Exception as e:
        logger.info('Model %s not found. Downloading...', str(model))
        try:
            ollama.pull(model)
            logger.info('Model %s downloaded successfully.', str(model))
            return True
        except Exception as e:
            logger.error('Program exit on exception EXT-000003 = %s', str(e))
            sys.exit()
