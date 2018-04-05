#!/usr/bin/env python3
# encoding: utf-8
# by fixdq

import logging
import logging.config
from conf import settings


def get_logger(name):
    logging.config.dictConfig(settings.LOGGING_DICT)
    ll = logging.getLogger(name)
    return ll


