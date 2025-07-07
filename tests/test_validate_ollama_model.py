#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import source.modules.functions.validate_ollama_model as validate_ollama_model


@pytest.fixture
def function_input_1():
    model = "mistral"
    return model


@pytest.fixture
def function_input_2():
    model_type = "ollama"
    return model_type


@pytest.fixture
def function_input_3():
    common_paths = [
        "/usr/local/bin/ollama",  # Default macOS install location
        "/opt/homebrew/bin/ollama",  # M1 Mac Homebrew location
        "ollama"  # If it's in PATH
    ]
    return common_paths


@pytest.fixture
def function_input_4():
    ollama_url = "http://localhost:11434"
    return ollama_url


@pytest.fixture
def function_input_5():
    ollama_models_url = "http://localhost:11434/api/tags"
    return ollama_models_url


@pytest.fixture
def function_input_6():
    auto_yes = False
    return auto_yes


@pytest.fixture
def function_output():
    return True


def test_validate_ollama_model(function_input_1, function_input_2, function_input_3, function_input_4, function_input_5, function_input_6, function_output):
    """
    Tests for `validate_ollama_model` package.
    Validate if the model exists for the given model type.

    :param : model
    :rtype: str
    :param : model_type
    :rtype: str
    :param : common_paths
    :rtype: list
    :param : ollama_url
    :rtype: str
    :param : ollama_models_url
    :rtype: str
    :param : auto_yes
    :rtype: bool
    :return: boolean
    :rtype: bool
    """

    assert function_output == validate_ollama_model.validate_ollama_model(function_input_1, function_input_2, function_input_3, function_input_4, function_input_5, function_input_6)
