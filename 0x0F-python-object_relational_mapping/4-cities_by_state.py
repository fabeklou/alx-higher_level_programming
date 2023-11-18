#!/usr/bin/python3

"""
This script lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    user_name = sys.argv[1]
    user_password = sys.argv[2]
    db_name = sys.argv[3]

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
                        SELECT cities.id, cities.name, states.name
                        FROM cities
                        LEFT JOIN states ON
                        cities.state_id = states.id
                        ORDER BY cities.id ASC
                        """)
    cities_by_state = db_cursor.fetchall()

    for citie in cities_by_state:
        print(citie)

    db_cursor.close()
    db_connection.close()
