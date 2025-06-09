#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import source.modules.functions.test_prompt as test_prompt


@pytest.fixture
def function_input_1():
    client = ""
    return client


@pytest.fixture
def function_input_2():
    model = "mistral:7b"
    return model


@pytest.fixture
def function_input_3():
    model_type = "ollama"
    return model_type


@pytest.fixture
def function_input_4():
    system_prompt = ""
    return system_prompt


@pytest.fixture
def function_input_5():
    test_prompt = ""
    return test_prompt


@pytest.fixture
def function_output():
    result = "Hello!"
    return result


def test_test_prompt(function_input_1, function_input_2, function_input_3, function_input_4, function_input_5, function_output):
    """
    Tests for `test_prompt` package.
    Validate if the model exists for the given model type.

    :param : client
    :rtype: str
    :param : model
    :rtype: str
    :param : model_type
    :rtype: str
    :param : system_prompt
    :rtype: str
    :param : test_prompt
    :rtype: str
    :return: tuple
    :rtype: str,bool
    """

    x = test_prompt.test_prompt(function_input_1, function_input_2, function_input_3, function_input_4, function_input_5)
    y = str(x[0])
    test = y[1:7]
    assert function_output == test
