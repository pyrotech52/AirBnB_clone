#!/usr/bin/python3
"""This module defines a base class for all models"""
import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

class BaseModel:
    """Base class for all models."""
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            if 'id' not in kwargs:
                kwargs['id'] = str(uuid.uuid4())
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                kwargs['created_at'] = datetime.now()
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                kwargs['updated_at'] = datetime.now()
            if '__class__' in kwargs:
                del kwargs['__class__']
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        Returns:
            str: String representation.
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.
        Returns:
            dict: Dictionary representation.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict


