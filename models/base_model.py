#!/usr/bin/python3
""" base class of all our models. """


class BaseModel():
""" base class defined """    
    

    def __init__(self):
        self.name = ""
        self.id = str(uuid.uuid4())
        self.created_at = ""
        self.updated_at = ""


        def save(self):
            pass

        def to_dict(self):
            return __dict__.keys

        def to_json():
            pass
