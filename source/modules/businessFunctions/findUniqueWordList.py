# -*- coding: utf-8 -*-
import sys
import source.modules.utils.logger as utils

__all__ = ['find_unique_word_list']


def find_unique_word_list(text):
    """
    Built from a text the list of words without repetition and return the result to the caller

    Exception management :
    If any exception : log the trace of the exception stack and stop the execution of the programme

    :param text: Text in RTF or TXT format
    :type text: str
    :return: The list of words that make up this text without repetitions
    :rtype: dict
    """
    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Start of function find_unique_word_list, input text len = %s', str(len(text)))

    try:
        result = []
        word_list = text.split()
        try:
            for word in word_list:
                if word not in result:
                    result.append(word)
            return result
        except Exception as e:
            logger.error('Exception : problem during text reading to extract words = %s', str(e))
            sys.exit()
    except Exception as e:
        logger.error('Exception : problem during text splitting = %s', str(e))
        sys.exit()
