#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import source.modules.businessFunctions.findUniqueWordList as findUniqueWordList


@pytest.fixture
def function_input():
    text = "Lorem ipsum dolor sit amet lorem sit dolor"
    return text


@pytest.fixture
def function_output():
    text = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'lorem']
    return text


def test_find_unique_word_list(function_input, function_output):
    """
    Tests for `find_unique_word_list` package.
    Check that the text is correctly cut out a list of words without repetition

    :param function_input: the text to be cut
    :type function_input: str
    :param function_output: list of words of the text without repetition
    :type function_output: dict
    """

    assert function_output == findUniqueWordList.find_unique_word_list(function_input)
