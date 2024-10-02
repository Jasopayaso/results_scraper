#!usr/bin/env python3
"""
Configuration for application

Used to provide environment-based configurations
"""

import os
import logging

class Config:
    PREM_BASE_RESULT_URL = 'https://www.premierleague.com/results'
    DEBUG = False
    REMOTE_SELENIUM = os.environ.get('REMOTE_SELENIUM', 'http://selenium:4444/wd/hub' )
    LOGGING_LEVEL = logging.INFO
