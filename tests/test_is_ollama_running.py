#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import source.modules.functions.is_ollama_running as is_ollama_running


@pytest.fixture
def function_input():
    ollama_url = "http://localhost:11434/"
    return ollama_url


@pytest.fixture
def function_output():
    return True


def test_is_ollama_running(function_input, function_output):
    """
    Tests for `is_ollama_running` package.
    Check if ollama is running on the computer and send back true

    :param: ollama_models_url, local url for ollama model, like http://localhost:11434/api/tags
    :ptype: str
    :return: boolean response is False or True if model running
    :rtype: bool
    """

    assert function_output == is_ollama_running.is_ollama_running(function_input)
