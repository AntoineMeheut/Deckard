#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from source.modules.functions import load_system_prompts


@pytest.fixture
def function_input_1():
    system_prompts_path = "../resource/system-prompts/system-prompts-normal.txt"
    return system_prompts_path


@pytest.fixture
def function_output_1():
    return "Vous êtes un assistant utile."


@pytest.fixture
def function_input_2():
    system_prompts_path = "../resource/none.txt"
    return system_prompts_path


@pytest.fixture
def function_output_2():
    return 'False'


def test_load_system_prompts_found(function_input_1, function_output_1):
    """
    Tests for `load_system_prompts` package.
    Try to load a file of prompts on the system and send back the prompts in the file.

    :param function_input: system_prompts_path
    :type function_input: str
    :param function_output: prompts
    :type function_output: str
    """

    assert function_output_1 == load_system_prompts.load_system_prompts(function_input_1)


def test_load_system_prompts_not_found(function_input_2, function_output_2):
    """
    Tests for `load_system_prompts` package.
    Try to load a file of prompts on the system and send back False if problem.

    :param function_input: system_prompts_path
    :type function_input: str
    :param function_output: error return
    :type function_output: str
    """

    assert function_output_2 == load_system_prompts.load_system_prompts(function_input_2)
