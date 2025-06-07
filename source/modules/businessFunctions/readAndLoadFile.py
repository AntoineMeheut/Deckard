# -*- coding: utf-8 -*-
import sys
import source.modules.utils.logger as utils

__all__ = ['read_and_load_file']


def read_and_load_file(filename):
    """
    Open a file, load it into a memory structure and return the memory structure to the caller

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme

    :param filename: Path and file name, format rtf or text
    :type filename: str
    :return: What was read in the file
    :rtype: str
    """
    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Start of function read_and_load_file, filename to read = %s', str(filename))

    try:
        try:
            with open(filename, 'r') as file:
                file_contents = file.read()
                logger.info('End of function read_and_load_file')
            return file_contents
        except IOError as e:
            logger.error('IOError = %s', str(e))
            sys.exit()
    except Exception as e:
        logger.error('Exception = %s', str(e))
        sys.exit()
    finally:
        file.close()
