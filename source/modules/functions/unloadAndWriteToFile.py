# -*- coding: utf-8 -*-
import sys
import source.modules.utils.logger as utils

__all__ = ['unload_and_write_to_file']


def unload_and_write_to_file(memory_structure, filename):
    """
    Unloads a structure in memory and writes it to a text file

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme

    :param memory_structure: Word list format structure
    :type memory_structure: dict
    :param filename: Name of the output file
    :type filename: str
    :return: Nothing
    """
    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Start of function unload_and_write_to_file, filename to write = %s, memory_structure len = %s',
                str(filename), str(len(memory_structure)))

    try:
        try:
            with open(filename, 'w') as file:
                for word in memory_structure:
                    file.write(str(word) + "\n")
                logger.info('End of function unload_and_write_to_file')
        except IOError as e:
            logger.error('IOError = %s', str(e))
            sys.exit()
    except Exception as e:
        logger.error('Exception = %s', str(e))
        sys.exit()
    finally:
        file.close()
