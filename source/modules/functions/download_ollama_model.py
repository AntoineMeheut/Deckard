# -*- coding: utf-8 -*-
import sys
import subprocess
import source.modules.utils.logger as utils


__all__ = ['download_ollama_model']

from source.modules.functions.get_ollama_path import get_ollama_path


def download_ollama_model(model: str, common_paths: list) -> bool:
    """
    Download an Ollama model.

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme.

    The program stops with a log with the exit code EXT-000002.

    :param: model is the model name like "mistral:7b"
    :ptype: str
    :param: common_paths is the ollama computer path, like : /usr/local/bin/ollama or /opt/homebrew/bin/ollama or ollama
    :ptype: list
    :return: boolean is False if ollama path not found or True if found
    :rtype: bool
    """

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Function download_ollama_model: starting downloading an Ollama model...')

    try:
        ollama_path = get_ollama_path(common_paths)
        # Run the command and let it inherit the parent's stdout/stderr directly
        result = subprocess.run([ollama_path, "pull", model], check=False)
        return result.returncode == 0
    except Exception as e:
        logger.error('Function download_ollama_model: exit on exception EXT-000002 = %s', str(e))
        sys.exit()
