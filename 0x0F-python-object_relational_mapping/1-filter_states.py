#!/usr/bin/python3

"""
This script lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

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
                        SELECT *
                        FROM states
                        WHERE name LIKE 'N%'
                        ORDER BY states.id ASC
                        """)
    states = db_cursor.fetchall()

    for state in states:
        print(state)

    db_cursor.close()
    db_connection.close()
