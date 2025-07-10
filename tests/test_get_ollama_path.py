#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import source.modules.functions.get_ollama_path as get_ollama_path


@pytest.fixture
def function_input():
    common_paths = [
        "/usr/local/bin/ollama",  # Default macOS install location
        "/opt/homebrew/bin/ollama",  # M1 Mac Homebrew location
        "ollama"  # If it's in PATH
    ]
    return common_paths


@pytest.fixture
def function_output():
    paths = "/usr/local/bin/ollama"  # Default macOS install location
    return paths


def test_get_ollama_path(function_input, function_output):
    """
    Tests for `get_ollama_path` package.
    Check if ollama is install on the computer and send back the ollama path

    :param: common_paths is the ollama computer path, like : /usr/local/bin/ollama or /opt/homebrew/bin/ollama or ollama
    :ptype: list
    :return: path is the ollama computer path, like : /usr/local/bin/ollama on macbook
    :rtype: str
    """

    assert function_output == get_ollama_path.get_ollama_path(function_input)
