#!/usr/bin/python3

"""
This script Improve the files model_city.py and model_state.py,
and save them as relationship_city.py and relationship_state.py
"""


if __name__ == "__main__":
    from relationship_state import Base
    from relationship_state import State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.engine import URL
    from sqlalchemy.orm import Session
    import sys

    user_name = sys.argv[1]
    user_password = sys.argv[2]
    db_name = sys.argv[3]

    url_object = URL.create(
        "mysql",
        username=user_name,
        password=user_password,
        host="localhost",
        port=3306,
        database=db_name
    )

    engine = create_engine(url_object)
    Base.metadata.create_all(engine)
    session = Session(engine)

    new_state = State(name='California')
    new_city = City(name='San Francisco')

    new_state.cities.append(new_city)
    session.add(new_state)

    session.commit()
    session.close()
