# -*- coding: utf-8 -*-
import os

import source.modules.utils.logger as utils


__all__ = ['load_system_prompts']


def load_system_prompts(system_prompts_path: str) -> str:
    """
    Load system prompts from the specified file.

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme

    :param : common_paths
    :rtype: str
    :return: boolean
    :rtype: bool
    """

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Starting loading system prompts from the specified file...')

    try:
        if not os.path.exists(system_prompts_path):
            logger.error('File not found = %s', str(system_prompts_path))
            return "False"
        else:
            with open(system_prompts_path, 'r', encoding='utf-8') as f:
                return f.read().strip()
    except FileNotFoundError as e:
        logger.error('Exception = %s', str(e))
        return "False"
