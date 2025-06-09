# -*- coding: utf-8 -*-
import sys
from typing import List
import source.modules.utils.logger as utils

__all__ = ['get_system_prompt_words']


def get_system_prompt_words(system_prompt: str, num_lines: int = 3) -> List[str]:
    """
    Extract unique words from the first N lines of system prompt.

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme

    :param : system_prompt
    :rtype: str
    :param : num_lines
    :rtype: int
    :return: str_list
    :rtype: list
    """

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Starting extract unique words from the first N lines of system prompt...')

    try:
        # Get first N lines
        lines = system_prompt.split('\n')[:num_lines]

        # Join lines and split into words
        words = ' '.join(lines).lower().split()

        # Remove common words and punctuation
        common_words = {'a', 'an', 'the', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from', 'and', 'or', 'but',
                        'can', 'do', 'does'}
        clean_words = []
        for word in words:
            # Remove punctuation
            word = ''.join(c for c in word if c.isalnum())
            if word and word not in common_words:
                clean_words.append(word)
        return clean_words
    except FileNotFoundError as e:
        logger.error('Exception = %s', str(e))
        sys.exit()
