#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey


class City(Base, BaseModel):
    """Defines City class that inherits from Base and BaseModel classes"""
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60),ForeignKey("states.id"), nullable=False)
