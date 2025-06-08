#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import source.modules.functions.validate_api_keys as validate_api_keys


@pytest.fixture
def function_input():
    model_type = "openai"
    return model_type


@pytest.fixture
def function_output():
    return False


def test_validate_api_keys(function_input, function_output):
    """
    Tests for `is_ollama_running` package.
    Check if ollama is running on the computer and send back true

    :param function_input: common_paths
    :type function_input: str
    :param function_output: boolean
    :type function_output: bool
    """

    assert function_output == validate_api_keys.validate_api_keys(function_input)
