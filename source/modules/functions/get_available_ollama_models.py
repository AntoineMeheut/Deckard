# -*- coding: utf-8 -*-
import sys
from typing import List

import requests

import source.modules.utils.logger as utils

__all__ = ['get_available_ollama_models']


def get_available_ollama_models(ollama_models_url: str) -> List[str]:
    """
    Get list of available Ollama models.

    Function input: ollama local server url

    Function output: list of all available ollama model on this local server

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme.

    The program stops with a log with the exit code EXT-000005.

    :param : ollama_models_url
    :rtype: str
    :return: str_list
    :rtype: list
    """

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Starting get list of available Ollama models...')

    try:
        response = requests.get(ollama_models_url)
        if response.status_code == 200:
            models = response.json().get("models", [])
            # Return both full names and base names without tags
            model_names = []
            for model in models:
                name = model["name"]
                model_names.append(name)
                # Add base name without tag
                if ":" in name:
                    model_names.append(name.split(":")[0])
            return model_names
        return []
    except Exception as e:
        logger.error('Program exit on exception EXT-000005 = %s', str(e))
        sys.exit()