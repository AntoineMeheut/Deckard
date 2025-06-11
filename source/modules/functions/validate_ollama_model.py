# -*- coding: utf-8 -*-
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
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme

    :param : model
    :rtype: str
    :param : model_type
    :rtype: str
    :param : common_paths
    :rtype: list
    :param : ollama_url
    :rtype: str
    :param : ollama_models_url
    :rtype: str
    :param : auto_yes
    :rtype: bool
    :return: boolean
    :rtype: bool
    """

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Starting to validate if the model exists for the given model type...')

    try:
        if model_type == "ollama":
            if not is_ollama_running(ollama_url):
                if not start_ollama(common_paths, ollama_url):
                    logger.error("Error: Could not start Ollama server")
                    return False
            available_models = get_available_ollama_models(ollama_models_url)
            if model not in available_models:
                print(f"Model '{model}' not found in Ollama.")
                logger.info("Model %s not found in Ollama", str(model))
                # Show available models without duplicates
                unique_models = sorted(set(m.split(":")[0] for m in available_models))
                print("Available models:", ", ".join(unique_models) if unique_models else "No models found")

                if auto_yes:
                    print(f"\nAutomatically downloading {model}...")
                    return download_ollama_model(model, common_paths)

                response = input(f"\nWould you like to download {model}? [y/N] ").lower().strip()
                if response == 'y' or response == 'yes':
                    print(f"\nDownloading {model}...")
                    return download_ollama_model(model, common_paths)
                else:
                    print("Download cancelled")
                    return False
        return True
    except Exception as e:
        logger.error('Exception = %s', str(e))
        return False
