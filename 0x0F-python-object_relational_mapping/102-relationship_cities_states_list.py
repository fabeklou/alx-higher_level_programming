#!/usr/bin/python3

"""
This script lists all City objects from the database hbtn_0e_101_usa
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy.engine import URL
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import State
    from relationship_city import City

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

    cities = session.query(City).join(State).order_by(City.id).all()

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
