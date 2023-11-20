#!/usr/bin/python3

"""
This script prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    from model_state import Base
    from model_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.engine import URL
    from sqlalchemy.orm import sessionmaker
    import sys

    user_name = sys.argv[1]
    user_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

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

    state_by_name = session.query(State).filter(
                    State.name == state_name).first()

    if state_by_name:
        print("{}".format(state_by_name.id))
    else:
        print("Not found")

    session.close()
