#!/usr/bin/python3

"""
State Module
"""
from models.base_model import BaseModel


class State(BaseModel):
    """class State"""

    name = ""

    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self, *args, **kwargs)
