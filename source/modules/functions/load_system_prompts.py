# -*- coding: utf-8 -*-
import os
import sys
import source.modules.utils.logger as utils

__all__ = ['load_system_prompts']


def load_system_prompts(system_prompts_path: str) -> str:
    """
    Load system prompts from the specified file.

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme.

    The program stops with a log with the exit code EXT-000010.

    :param: system_prompts_path, the path to the system prompt files
    :ptype: str
    :return: system_prompt, the prompt system which can modify the operation of the model, like You are an helpful assistant. Answer questions about users food deliveries..
    :rtype: str
    """

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Function load_system_prompts: loading system prompts from the specified file...')

    try:
        if not os.path.exists(system_prompts_path):
            logger.error('Function load_system_prompts: file not found = %s', str(system_prompts_path))
            return "False"
        else:
            with open(system_prompts_path, 'r', encoding='utf-8') as f:
                return f.read().strip()
    except FileNotFoundError as e:
        logger.error('Function load_system_prompts: exit on exception EXT-000010 = %s', str(e))
        sys.exit()
