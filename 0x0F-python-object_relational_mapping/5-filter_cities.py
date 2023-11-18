#!/usr/bin/python3

"""
This script takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    user_name = sys.argv[1]
    user_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_name,
        passwd=user_password,
        db=db_name,
        charset="utf8"
    )

    db_cursor = db_connection.cursor()
    db_cursor.execute("""
                        SELECT cities.name
                        FROM cities
                        LEFT JOIN states ON
                        states.id = cities.state_id
                        WHERE states.name LIKE BINARY %s
                        """, (state_name,))
    filter_cities = db_cursor.fetchall()

    f_cities = ""
    for citie in filter_cities:
        f_cities += "{:s}, ".format(citie[0])
    print(f_cities[:-2])

    db_cursor.close()
    db_connection.close()
