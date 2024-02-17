#!/usr/bin/python3

"""This module lists all cities from the database hbtn_0e_4_usa

Command line Args:
    user (str): the mysql username
    passwd (str): the mysql password
    db (str): the database name

Constants:
    host (str): host name set to `localhost`
    port (int): port number set to `3306`

"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    # arguments passed to the module
    user, passwd, db = sys.argv[1:4]

    host, port = 'localhost', 3306

    # creating a connection object
    conn = MySQLdb.connect(
        host=host, port=port,
        user=user, passwd=passwd,
        db=db, charset='utf8'
    )

    # creating a cursor object
    cur = conn.cursor()

    cur.execute("""
                SELECT cities.id,
                    cities.name,
                    states.name
                FROM   cities
                    LEFT JOIN states
                            ON cities.state_id = states.id
                ORDER  BY cities.id ASC;
                """)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    # terminating the session
    cur.close()
    conn.close()
