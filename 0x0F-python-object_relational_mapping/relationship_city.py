#!/usr/bin/python3
"""
Relationships between states and cities usig SQLAlchemy module
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    state_id = Column(Integer, ForeignKey('state.id'))
    state = relationship('State', back_populates='cities')
