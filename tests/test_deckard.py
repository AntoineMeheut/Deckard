#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

import pytest
import source.main.deckard as deckard

@pytest.fixture
def function_input():
    # python3 deckard.py --model mistral:7b --model-type ollama
    parser = argparse.ArgumentParser(description="Test LLM system prompts against injection attacks")
    parser.add_argument("--model", required=True, help="LLM model name")
    parser.add_argument("--model-type", required=True, choices=["openai", "anthropic", "ollama"],
                        help="Type of the model (openai, anthropic, ollama)")
    parser.parse_known_args(['--model', 'mistral:7b', '--model-type', 'ollama'])
    print(parser)

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


