#!/usr/bin/python3
"""
Define a City model.
Inherits from SQLAlchemy Base and links to the MySQL table cities.
"""
from sqlalchemy import Column, Integer, String, ForeignKey, null
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """This defines the City class.

    Attributes:
        id (str): The city's id.
        name (sqlalchemy.Integer): The city's name.
        state_id (sqlalchemy,String): The city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
