# -*- coding: utf-8 -*-
"""
    @date: 12/24/18

"""

from enum import IntEnum

class Status(IntEnum):
    OK = 1
    NOT_OK = 2

    ERR = -1

class ErrorCode(IntEnum):
    NORMAL = -1
    HIGH = -10    
    CRITICAL = -100
    BLOCKING = -1000
