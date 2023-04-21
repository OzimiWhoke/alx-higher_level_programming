#!/usr/bin/python3
"""
Relationship between states and cities using SQLAlchemy module
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    cities = relationship('City', back_populates='state', cascade='all,delete')
