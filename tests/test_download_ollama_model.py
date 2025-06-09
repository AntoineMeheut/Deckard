#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import source.modules.functions.download_ollama_model as download_ollama_model


@pytest.fixture
def function_input_1():
    model = "mistral:7b"
    return model


@pytest.fixture
def function_input_2():
    common_paths = [
        "/usr/local/bin/ollama",  # Default macOS install location
        "/opt/homebrew/bin/ollama",  # M1 Mac Homebrew location
        "ollama"  # If it's in PATH
    ]
    return common_paths


@pytest.fixture
def function_output():
    return True


def test_download_ollama_model(function_input_1, function_input_2, function_output):
    """
    Tests for `download_ollama_model` package.
    Download the ollama model needed for the test session.

    :param : model
    :rtype: str
    :param : common_paths
    :rtype: list
    :return: boolean
    :rtype: bool
    """

    assert function_output == download_ollama_model.download_ollama_model(function_input_1, function_input_2)
