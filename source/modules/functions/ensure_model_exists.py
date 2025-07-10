# -*- coding: utf-8 -*-
import sys
import ollama

import source.modules.utils.logger as utils

__all__ = ['ensure_model_exists']


def ensure_model_exists(model: str):
    """
    Ensure the Ollama model exists, download if not.

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme.

    The program stops with a log with the exit code EXT-000003.

    :param: model is the model name like "mistral:7b"
    :ptype: str
    :return: none, the program stops if it does not find the model
    :rtype: none
    """

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Function ensure_model_exists: check if ollama model exist...')

    try:
        ollama.list(model)
        return None
    except Exception as e:
        logger.info('Function ensure_model_exists: model %s not found. Downloading...', str(model))
        try:
            ollama.pull(model)
            logger.info('Function ensure_model_exists: model %s downloaded successfully.', str(model))
            return True
        except Exception as e:
            logger.error('Function ensure_model_exists: exit on exception EXT-000003 = %s', str(e))
            sys.exit()
