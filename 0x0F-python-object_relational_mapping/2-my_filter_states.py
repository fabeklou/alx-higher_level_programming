#!/usr/bin/python3

"""This module takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where
name matches the argument

Command line Args:
    user (str): the mysql username
    passwd (str): the mysql password
    db (str): the database name
    name (str): state name searched

Constants:
    host (str): host name set to `localhost`
    port (int): port number set to `3306`

"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    # arguments passed to the module
    user, passwd, db, name = sys.argv[1:5]

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
                WHERE  states.name LIKE BINARY '{}'
                ORDER  BY states.id ASC;
                """.format(name))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    # terminating the session
    cur.close()
    conn.close()
