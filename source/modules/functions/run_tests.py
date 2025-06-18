# -*- coding: utf-8 -*-
import sys
from typing import Dict
import source.modules.utils.logger as utils
from source.modules.functions.initialize_client import initialize_client
from source.modules.functions.load_system_prompts import load_system_prompts
from source.modules.functions.load_test_rules import load_test_rules
from source.modules.functions.run_single_test import run_single_test
from source.modules.functions.validate_api_keys import validate_api_keys

__all__ = ['run_tests']


def run_tests(model: str, model_type: str, system_prompts_path: str, common_paths: list, ollama_url: str,
              iterations: int = 5, severities: list = None, rule_names: list = None, firewall_mode: bool = False,
              pass_condition: str = None) -> Dict[str, dict]:
    """
    Run all tests and return results.

    Function input:

    Function output:

    Exception management :
    If IOError or any exception : log the trace of the exception stack and stop the execution of the programme.

    The program stops with a log with the exit code EXT-000013.

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
    logger.info('Function run_tests: starting to initialize the appropriate client based on the model type....')

    try:

        if not validate_api_keys(model_type):
            logger.error('Function run_tests: no KEY environment variable found, it is required')
            sys.exit()

        client = initialize_client(model_type, common_paths, ollama_url)

        if client == "False":
            logger.error('Function run_tests: no openai, anthropic or ollama client running, it is required')
            sys.exit()

        system_prompt = load_system_prompts(system_prompts_path)

        if system_prompt == "False":
            logger.error('Function run_tests: no prompts file found, it is required')
            sys.exit()
        results = {}

        if firewall_mode and not pass_condition:
            raise ValueError("Pass condition must be specified when using firewall mode")

        test_rules = load_test_rules(0, 0)

        # Filter rules based on severity and rule names
        filtered_rules = {}
        for test_name, rule in test_rules.items():
            # Check if rule matches both severity and name filters (if any)
            severity_match = not severities or rule['severity'] in severities
            name_match = not rule_names or test_name in rule_names

            if severity_match and name_match:
                filtered_rules[test_name] = rule

        if rule_names and len(filtered_rules) < len(rule_names):
            # Find which requested rules don't exist
            missing_rules = set(rule_names) - set(filtered_rules.keys())
            logger.info('Function run_tests: the following requested rules were not found: %s', str(missing_rules))

        total_filtered = len(filtered_rules)

        if total_filtered == 0:
            logger.info('Function run_tests: no rules matched the specified criteria')
            return results

        for i, (test_name, rule) in enumerate(filtered_rules.items(), 1):
            print(f"\nFunction run_tests: Running test [{i}/{total_filtered}]: {test_name} ({rule['type']}, severity: {rule['severity']})")
            result = run_single_test(client, model, model_type, system_prompt, test_name, rule, iterations, firewall_mode,
                                     pass_condition)

            # Print summary
            if result["passed"]:
                logger.info('Function run_tests: test passed, result = %s', str(result['pass_rate']))
                print(f"Function run_tests: test passed, result = {result['pass_rate']}.")
            else:
                if result.get("failed_result", {}).get("reason", "").startswith("API Error:"):
                    logger.info('Function run_tests: test failed, result, result = %s', str(result['pass_rate']))
                    print(f"Function run_tests: test failed, result = {result['pass_rate']}.")
                    # Stop testing if we get an API error
                    logger.info('Function run_tests: stopping tests due to API error.')
                    results[test_name] = result
                    return results
                else:
                    logger.info('Function run_tests: final result = %s', str(result['pass_rate']))
                    print(f"Function run_tests: final result = {result['pass_rate']}.")
            results[test_name] = result
        logger.info('Function run_tests: All tests completed.')
        print(f"Function run_tests: All tests completed.")

        return results
    except Exception as e:
        logger.error('Function run_tests: exit on exception EXT-000013 = %s', str(e))
        sys.exit()
