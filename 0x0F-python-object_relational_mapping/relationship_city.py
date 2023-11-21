#!/usr/bin/python3

"""
This module contains the class definition of a City
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from relationship_state import Base


class City(Base):
    """
    The Citit class maps <City object> to the <cities table>

    Args:
        __tablename__ (str): name of the mapping table
        id (int): the unique id
        name (str): the value, name of a city
        state_id (int): state id

    """
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
