#!/usr/bin/python3

"""This module contains the class definition of a State
and an instance Base = declarative_base()

"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """
    The State class maps <state objects> to the <states table>

    Args:
        __tablename__ (str): name of the table
        id (int): a column/attribute in the table, repr the PK
        name (str): a column/attribute in the table, repr
            the name of a state

    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
