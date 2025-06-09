# -*- coding: utf-8 -*-
import sys
import glob
import yaml
from typing import Dict

import source.modules.utils.logger as utils

__all__ = ['load_test_rules']


def load_test_rules(rule_start, rule_stop) -> Dict[str, dict]:
    """
    Load all test rules from YAML files in the rules directory.

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme

    :param : rule_start
    :rtype: int
    :param : rule_stop
    :rtype: int
    :return: Dict
    :rtype: str, dict
    """

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Starting loading test rules...')

    try:
        rules = {}
        rule_files = glob.glob("../resource/voight-kampff/*.yaml")
        if rule_start == 0:
            for rule_file in rule_files:
                with open(rule_file, 'r', encoding='utf-8') as f:
                    rule = yaml.safe_load(f)
                    rules[rule['name']] = rule
            return rules
        else:
            i = rule_start
            while i <= rule_stop:
                rule_file = rule_files[i]
                with open(rule_file, 'r', encoding='utf-8') as f:
                    rule = yaml.safe_load(f)
                    rules[rule['name']] = rule
                i += 1
            return rules
    except FileNotFoundError as e:
        logger.error('Exception = %s', str(e))
        sys.exit()
