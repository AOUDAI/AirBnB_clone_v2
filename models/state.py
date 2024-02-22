#!/usr/bin/python3
"""Contains the class State"""

from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """State class that inherites from Base and BaseModel classes"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all")

    @property
    def cities(self):
        myCities = [city for city in self.cities if city.state_id == self.id]
        return myCities
