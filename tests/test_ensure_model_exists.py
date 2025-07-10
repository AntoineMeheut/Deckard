#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import source.modules.functions.ensure_model_exists as ensure_model_exists


@pytest.fixture
def function_input():
    model = "mistral:7b"
    return model


@pytest.fixture
def function_output():
    return True


def test_ensure_model_exists(function_input, function_output):
    """
    Tests for `is_ollama_running` package.
    Check if ollama is running on the computer and send back true

    :param: model is the model name like "mistral:7b"
    :ptype: str
    :return: none, the program stops if it does not find the model
    :rtype: none
    """

    assert function_output == ensure_model_exists.ensure_model_exists(function_input)
