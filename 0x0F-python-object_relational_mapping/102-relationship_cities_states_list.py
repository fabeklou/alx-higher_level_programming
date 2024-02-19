#!/usr/bin/python3

"""This module lists all City objects from
the database hbtn_0e_101_usa

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

    cities = session.query(City).join(State).order_by(City.id).all()

    for city in cities:
        print("{}: {}  -> {}".format(
            city.id, city.name, city.state.name))

    session.close()
