#!/usr/bin/python3

"""
This script adds the State object “Louisiana” to the database hbtn_0e_6_usa
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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print("{}".format(new_state.id))

    session.close()
