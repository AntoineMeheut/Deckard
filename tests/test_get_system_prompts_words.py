#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import source.modules.functions.get_system_prompt_words as get_system_prompt_words


@pytest.fixture
def function_input_1():
    system_prompt = "You are an helpful assistant. Answer questions about users food deliveries."
    return system_prompt


@pytest.fixture
def function_input_2():
    num_lines = 1
    return num_lines


@pytest.fixture
def function_output():
    str_list = ['you',
                'are',
                'helpful',
                'assistant',
                'answer',
                'questions',
                'about',
                'users',
                'food',
                'deliveries']
    return str_list


def test_get_system_prompt_words(function_input_1, function_input_2, function_output):
    """
    Tests for `is_ollama_running` package.
    Check if ollama is running on the computer and send back true

    :param: system_prompt, the prompt system which can modify the operation of the model, like You are an helpful assistant. Answer questions about users food deliveries..
    :ptype: str
    :param: num_lines, the number of lines in the system prompt, like 1 line
    :ptype: int
    :return: str_list, the words in the system prompt like 'you', 'are', 'helpful', 'assistant', 'answer', 'questions', 'about', 'users', 'food', 'deliveries'
    :rtype: list
    """

    assert function_output == get_system_prompt_words.get_system_prompt_words(function_input_1, function_input_2)
