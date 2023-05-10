#!/usr/bin/python3

"""Amenity Module"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity"""

    name = ""

    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self, *args, **kwargs)
