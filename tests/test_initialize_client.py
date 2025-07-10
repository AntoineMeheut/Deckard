#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from source.modules.functions import initialize_client


@pytest.fixture
def function_input_1():
    model_type = "ollama"
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

    :param: model_type like ollama or openai or anthropic
    :ptype: str
    :param: common_paths is the ollama computer path, like : /usr/local/bin/ollama or /opt/homebrew/bin/ollama or ollama
    :ptype: list
    :param: ollama_models_url, local url for ollama model, like http://localhost:11434/api/tags
    :ptype: str
    :return: none
    :rtype: none
    """

    assert function_output == initialize_client.initialize_client(function_input_1, function_input_2, function_input_3)
