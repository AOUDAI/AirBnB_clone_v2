#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
import models
import uuid


Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    create_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs.pop('__class__', None)
            for key, value in kwargs.items():
                setattr(self, key, value)
            to_time = datetime.strptime
            self.created_at = to_time(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = to_time(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")


    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        myDict = self.__dict__.copy()
        myDict["__class__"] = self.__class__.__name__
        myDict['created_at'] = self.created_at.isoformat()
        myDict['updated_at'] = self.updated_at.isoformat()
        myDict.pop("_sa_instance_state", None)
        return myDict
    
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)