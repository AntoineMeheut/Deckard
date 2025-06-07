# -*- coding: utf-8 -*-

import argparse
import sys
from ..modules.businessFunctions.findUniqueWordList import find_unique_word_list
from ..modules.businessFunctions.unloadAndWriteToFile import unload_and_write_to_file
from ..modules.businessFunctions.readAndLoadFile import read_and_load_file
from ..modules.utils.logger import setup_logging

__all__ = ['arg_parser']


def arg_parser(parser):
    """
    Console script for main

    :param parser: The parser variable that contains the arguments passed to the program when it was launched
    :type parser: dict
    :return: Arguments parsed for use by the program
    :rtype: dict
    """
    logging = setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Start of function arg_parser, input = %s', str(parser))

    parser.add_argument('_', nargs='*')
    args = parser.parse_args()
    print("Arguments: " + str(args._)) # TODO - Test and suppress this print

    logger.info('Start of function arg_parser, ouput = %s', str(args))
    return args


def main(parser):
    """
    Call the function that parses the arguments and perform the orchestration of this program using
    the functions that will realize the transformation value

    :param parser: The arguments passed to the program when it was launched
    :type parser: dict
    :return: None
    """
    logging = utils.logger.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Start of program Unique Word List')

    args = arg_parser(parser)

    file = str(args)
    text = read_and_load_file(file)
    result = find_unique_word_list(text)
    unload_and_write_to_file(result)

    logger.info('End of program Unique Word List')
    return 0


if __name__ == "__main__":
    """
    Execute a sys.exit and call the main program giving it the arguments passed to the program at the time of execution
    
    """
    sys.exit(main(argparse.ArgumentParser()))  # pragma: no cover
