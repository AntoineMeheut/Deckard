#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import source.modules.functions.start_ollama as start_ollama


@pytest.fixture
def function_input_1():
    common_paths = [
        "/usr/local/bin/ollama",  # Default macOS install location
        "/opt/homebrew/bin/ollama",  # M1 Mac Homebrew location
        "ollama"  # If it's in PATH
    ]
    return common_paths


@pytest.fixture
def function_input_2():
    ollama_url = "http://localhost:11434"
    return ollama_url


@pytest.fixture
def function_output():
    return True


def test_start_ollama(function_input_1, function_input_2, function_output):
    """
    Tests for `is_ollama_running` package.
    Check if ollama is running on the computer and send back true

    :param: common_paths is the ollama computer path, like : /usr/local/bin/ollama or /opt/homebrew/bin/ollama or ollama
    :ptype: list
    :return: boolean, return True if ollama is running
    :rtype: bool
    """

    assert function_output == start_ollama.start_ollama(function_input_1, function_input_2)
