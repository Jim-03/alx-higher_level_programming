#!/usr/bin/python3
""" Class defining a state with a relationship to cities """
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ Defines a state with a relationship to cities """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state",
                          cascade="all, delete, delete-orphan")
