#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging.config
import yaml

__all__ = ['setup_logging']


def setup_logging(default_path='logging.yaml', default_level=logging.INFO, env_key='LOG_CFG'):
    """
    Setup logging configuration

    Writes a log in the target type configured in the logger.yaml file (this component manages log levels,
    calling components, the log target to the console or a log file and format).

    If you want to know more about log : https://docs.python.org/3/howto/logging.html#logging-advanced-tutorial

    :return: logging configuration
    :rtype: module
    """

    path = './resource/' + default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

    return logging
