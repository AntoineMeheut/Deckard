# -*- coding: utf-8 -*-
import sys
import tiktoken
import source.modules.utils.logger as utils

__all__ = ['count_tokens']


def count_tokens(text: str) -> int:
    """
    Count the number of tokens in a text using GPT tokenizer.

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme.
    The program stops with a log with the exit code EXT-000001.

    :param : text
    :rtype: str
    :return: number_of_token
    :rtype: int
    """

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Starting counting the number of tokens in a text using GPT tokenizer...')

    try:
        encoder = tiktoken.get_encoding("cl100k_base")  # Using Claude's encoding, works well for general text
        return len(encoder.encode(text))
    except Exception as e:
        logger.error('Program exit on exception EXT-000001 = %s', str(e))
        sys.exit()
