#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import source.modules.functions.is_ollama_running as is_ollama_running


@pytest.fixture
def function_input():
    ollama_url = "https://www.ollama.url.test"
    return ollama_url


@pytest.fixture
def function_output():
    return False


def test_is_ollama_running(function_input, function_output):
    """
    Tests for `is_ollama_running` package.
    Check if ollama is running on the computer and send back true

    :param function_input: ollama url
    :type function_input: str
    :param function_output: boolean
    :type function_output: bool
    """

    assert function_output == is_ollama_running.is_ollama_running(function_input)
