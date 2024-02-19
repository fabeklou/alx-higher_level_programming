#!/usr/bin/python3

"""This module contains the class definition of a city

"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    The  City class maps <city objects> to the <cities table>

    Args:
        __tablename__ (str): name of the table
        id (int): a column/attribute in the table, repr the PK
        state_id (int): a column/attribute in the table,
            repr the FK(states.id)
        name (str): a column/attribute in the table, repr
            the name of a city

    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
