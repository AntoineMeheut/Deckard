# -*- coding: utf-8 -*-
import sys
import glob
import yaml
from typing import Dict

import source.modules.utils.logger as utils

__all__ = ['load_test_rules']


def load_test_rules() -> Dict[str, dict]:
    """
    Load all test rules from YAML files in the rules directory.

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme

    :param : none
    :rtype: none
    :return: Dict
    :rtype: str, dict
    """

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Starting loading test rules...')

    try:
        rules = {}
        rule_files = glob.glob("ressource/voight-kampff/*.yaml")

        for rule_file in rule_files:
            with open(rule_file, 'r', encoding='utf-8') as f:
                rule = yaml.safe_load(f)
                rules[rule['name']] = rule
        return rules
    except FileNotFoundError as e:
        logger.error('Exception = %s', str(e))
        sys.exit()
