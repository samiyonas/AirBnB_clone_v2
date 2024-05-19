#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import String, Column, ForeignKey


class Amenity(BaseModel, Base):
    """ Amenities """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

