# -*- coding: utf-8 -*-
import sys
import source.modules.utils.logger as utils
from source.modules.functions.download_ollama_model import download_ollama_model
from source.modules.functions.get_available_ollama_models import get_available_ollama_models
from source.modules.functions.is_ollama_running import is_ollama_running
from source.modules.functions.start_ollama import start_ollama

__all__ = ['validate_ollama_model']


def validate_ollama_model(model: str, model_type: str, common_paths: list, ollama_url: str, ollama_models_url: str, auto_yes: bool = False) -> bool:
    """
    Validate if the model exists for the given model type.

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme.

    The program stops with a log with the exit code EXT-000017.

    :param: model is the model name like "mistral:7b"
    :ptype: str
    :param: model_type like ollama or openai or anthropic
    :ptype: str
    :param: common_paths is the ollama computer path, like : /usr/local/bin/ollama or /opt/homebrew/bin/ollama or ollama
    :ptype: list
    :param: ollama_url, local url for ollama, like http://localhost:11434
    :rtype: str
    :param: ollama_models_url, local url for ollama model, like http://localhost:11434/api/tags
    :ptype: str
    :param: auto_yes, setting to download the model automatically or not
    :rtype: boolean
    :return: True is model is validated else False
    :rtype: bool
    """

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Function validate_ollama_model: starting to validate if the model exists for the given model type...')

    try:
        if model_type == "ollama":
            if not is_ollama_running(ollama_url):
                if not start_ollama(common_paths, ollama_url):
                    logger.error("Function validate_ollama_model: could not start Ollama server")
                    return False
            available_models = get_available_ollama_models(ollama_models_url)
            if model not in available_models:
                logger.info("Function validate_ollama_model: model %s not found in Ollama", str(model))
                # Show available models without duplicates
                unique_models = sorted(set(m.split(":")[0] for m in available_models))
                if unique_models:
                    logger.info("Function validate_ollama_model: available models list is %s", str(unique_models))
                else:
                    logger.info("Function validate_ollama_model: no models found")
                if auto_yes:
                    logger.info("Function validate_ollama_model: automatically downloading %s model", str(model))
                    return download_ollama_model(model, common_paths)

                response = input(f"\nWould you like to download {model}? [y/N] ").lower().strip()
                if response == 'y' or response == 'yes':
                    print(f"\nDownloading {model}...")
                    logger.info("Function validate_ollama_model: downloading %s", str(model))
                    return download_ollama_model(model, common_paths)
                else:
                    logger.info("Function validate_ollama_model: download cancelled")
                    return False
        return True
    except Exception as e:
        logger.error('Function validate_ollama_model: exit on exception EXT-000017 = %s', str(e))
        sys.exit()
