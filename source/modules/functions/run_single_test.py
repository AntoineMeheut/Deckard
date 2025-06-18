# -*- coding: utf-8 -*-
import os
import sys
from typing import Dict
import source.modules.utils.logger as utils
from source.modules.functions.evaluate_test_result import evaluate_test_result
from source.modules.functions.test_prompt import test_prompt

__all__ = ['run_single_test']


def run_single_test(client, model: str, model_type: str, system_prompt: str,
                    test_name: str, rule: dict, num_runs: int = 5,
                    firewall_mode: bool = False, pass_condition: str = None) -> Dict:
    """
    Run a single test multiple times and evaluate results.

    Function input:

    Function output:

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme.

    The program stops with a log with the exit code EXT-000012.

    :param : client
    :rtype: str
    :param : model
    :rtype: str
    :param : model_type
    :rtype: str
    :param : system_prompt
    :rtype: str
    :param : test_name
    :rtype: str
    :param : rule
    :rtype: dict
    :param : num_runs
    :rtype: int
    :param : firewall_mode
    :rtype: bool
    :param : pass_condition
    :rtype: str
    :return: result
    :rtype: dict
    """

    logging = utils.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Function run_single_test: starting to run a single test multiple times and evaluate results...')

    try:

        failed_result = None
        passed_count = 0

        print(f"Running up to {num_runs} iterations.")
        logger.info('Running up to %s iterations', str(num_runs))

        for i in range(num_runs):
            response, is_error = test_prompt(client, model, model_type, system_prompt, rule['prompt'])
            passed, reason = evaluate_test_result(test_name, rule, response, is_error, system_prompt, firewall_mode,
                                              pass_condition)

            if passed:
                passed_count += 1
                logger.info('Function run_single_test: Iteration %s', str(passed_count))
            else:
                failed_result = {
                    "response": response,
                    "reason": reason
                }
                if reason.startswith("API Error:"):
                    logger.info('Function run_single_test: Iteration %s for reason %s', str(passed_count), str(reason))
                else:
                    logger.info('Function run_single_test: Iteration %s for reason %s', str(passed_count), str(reason))
                break  # Stop iterations on first failure

        overall_passed = passed_count == num_runs
        actual_runs = i + 1  # Number of actual iterations run

        result = {
            "type": rule['type'],
            "severity": rule['severity'],
            "passed": overall_passed,
            "pass_rate": f"{passed_count}/{actual_runs}"
        }

        # Only include failed result if there was a failure
        if failed_result:
            result["failed_result"] = failed_result
        return result
    except Exception as e:
        logger.error('Function run_single_test: exit on exception EXT-000012 = %s', str(e))
        sys.exit()
