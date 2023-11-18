#!/usr/bin/python3

"""
This script takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

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
                        SELECT *
                        FROM states
                        WHERE states.name LIKE BINARY '{}'
                        ORDER BY states.id ASC
                        """.format(state_name))
    states_by_name = db_cursor.fetchall()

    for state in states_by_name:
        print(state)

    db_cursor.close()
    db_connection.close()
