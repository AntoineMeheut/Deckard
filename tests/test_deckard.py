#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

import pytest
import source.main.deckard as deckard

@pytest.fixture
def function_input():
    parser = argparse.ArgumentParser(prog='deckard.py', usage='%(prog)s [options]')
    parser.parse_args(['--model', 'mistral:7b'])
    parser.parse_args(['--model-type', 'ollama'])
    return parser


@pytest.fixture
def function_output():
    text = "xxx"
    return text


def test_deckard(function_input, function_output):
    """
    Tests for main program `deckard`.

    Assert that deckard return the correct result.

    Input :

    :param function_input: deckard args
    :type function_input: str
    :param function_output: deckard result
    :type function_output: str
    """

    assert function_output == deckard.main(function_input)


