#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import argparse
import source.principal.cli as cli


@pytest.fixture
def function_input():
    text = argparse.ArgumentParser()
    return text


@pytest.fixture
def function_output():
    text = argparse.Namespace(_=['/Users/antoinemeheut/Documents/GitHub/UniqueWordList/tests/test_cli.py'])
    return text


def test_cli_arg_parser(function_input, function_output):
    """
    Tests for `cli` package.
    Assert that arg parser get the correct path and file

    :param function_input: path and python file
    :type function_input: str
    :param function_output: path and python file
    :type function_output: str
    """

    args = cli.arg_parser(function_input)
    assert args == function_output


