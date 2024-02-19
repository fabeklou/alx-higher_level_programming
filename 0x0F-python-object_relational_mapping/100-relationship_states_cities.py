#!/usr/bin/python3

"""This module creates the State "California" with
the City"San Francisco" from the database hbtn_0e_100_usa

"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == '__main__':
    # getting db connection infirmations from CLA
    user, passwd, db = sys.argv[1:4]

    # creating a new engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(user, passwd, db),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # creating a new session object
    session = Session(engine)

    # creating a state and a city object
    new_state = State(name="California")
    new_city = City(name="San Francisco")

    new_state.cities.append(new_city)
    session.add(new_state)
    session.commit()

    session.close()
