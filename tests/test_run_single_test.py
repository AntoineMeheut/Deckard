#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import source.modules.functions.run_single_test as run_single_test


@pytest.fixture
def function_input_1():
    client = ""
    return client


@pytest.fixture
def function_input_2():
    model = ""
    return model


@pytest.fixture
def function_input_3():
    model_type = ""
    return model_type


@pytest.fixture
def function_input_4():
    system_prompt = ""
    return system_prompt


@pytest.fixture
def function_input_5():
    test_name = ""
    return test_name


@pytest.fixture
def function_input_6():
    rule = ""
    return rule


@pytest.fixture
def function_input_7():
    num_runs = ""
    return num_runs


@pytest.fixture
def function_input_8():
    firewall_mode = ""
    return firewall_mode


@pytest.fixture
def function_input_9():
    pass_condition = ""
    return pass_condition


@pytest.fixture
def function_output():
    result = ""
    return result


def test_run_single_test(function_input_1, function_input_2, function_input_3, function_input_4, function_input_5, function_input_6, function_input_7, function_input_8, function_input_9, function_output):
    """
    Tests for `evaluate_test_result` package.
    Validate if the model exists for the given model type.

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

    assert function_output == run_single_test.run_single_test(function_input_1, function_input_2, function_input_3, function_input_4, function_input_5, function_input_6, function_input_7, function_input_9, function_input_9)
