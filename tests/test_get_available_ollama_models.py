#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import source.modules.functions.get_available_ollama_models as get_available_ollama_models


@pytest.fixture
def function_input():
    ollama_models_url = "http://localhost:11434/api/tags"
    return ollama_models_url


@pytest.fixture
def function_output():
    str_list = ['mistral:7b', 'mistral', 'mistral:latest', 'mistral']
    return str_list


def test_get_available_ollama_models(function_input, function_output):
    """
    Tests for `get_available_ollama_models` package.
    Check if ollama is running on the computer and send back true

    :param : ollama_models_url
    :rtype: str
    :return: str_list
    :rtype: list
    """

    assert function_output == get_available_ollama_models.get_available_ollama_models(function_input)
