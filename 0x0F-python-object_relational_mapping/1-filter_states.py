#!/usr/bin/python3

"""This module lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa

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
                SELECT *
                FROM   states
                WHERE  states.name LIKE BINARY 'N%'
                ORDER  BY states.id ASC;
                """)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    # terminating the session
    cur.close()
    conn.close()
