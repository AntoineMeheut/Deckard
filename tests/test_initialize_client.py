#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from source.modules.functions import initialize_client


@pytest.fixture
def function_input_1():
    model_type = "openai"
    return model_type


@pytest.fixture
def function_input_2():
    common_paths = [
        "/usr/local/bin/ollama",  # Default macOS install location
        "/opt/homebrew/bin/ollama",  # M1 Mac Homebrew location
        "ollama"  # If it's in PATH
    ]
    return common_paths


@pytest.fixture
def function_input_3():
    ollama_url = "http://localhost:11434"
    return ollama_url


@pytest.fixture
def function_output():
    return 'False'


def test_initialize_client(function_input_1, function_input_2, function_input_3, function_output):
    """
    Tests for `initialize_client` package.
    Check if ollama is running on the computer and send back true

    :param function_input: common_paths
    :type function_input: str
    :param function_output: boolean
    :type function_output: bool
    """

    assert function_output == initialize_client.initialize_client(function_input_1, function_input_2, function_input_3)
