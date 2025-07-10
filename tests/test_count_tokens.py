#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import source.modules.functions.count_tokens as count_tokens


@pytest.fixture
def function_input():
    text = "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do"
    return text


@pytest.fixture
def function_output():
    number_of_token = 10
    return number_of_token


def test_count_tokens(function_input, function_output):
    """
    Tests for `count_tokens` package.
    Check if ollama is install on the computer and send back the ollama path

    :param: text is a list of tokens like "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do"
    :ptype: str
    :return: number_of_token is the number of tokens counted like 10 in this case
    :rtype: int
    """

    assert function_output == count_tokens.count_tokens(function_input)
