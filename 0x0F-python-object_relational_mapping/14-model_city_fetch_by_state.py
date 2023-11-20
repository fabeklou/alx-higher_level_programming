#!/usr/bin/python3

"""
This script prints all City objects from the database hbtn_0e_14_usa
"""


if __name__ == "__main__":
    from model_state import Base
    from model_state import State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.engine import URL
    from sqlalchemy.orm import sessionmaker
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
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(City, State).join(State)

    for city, state in res.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
