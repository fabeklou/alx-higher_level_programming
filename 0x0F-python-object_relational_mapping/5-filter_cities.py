#!/usr/bin/python3

"""This module takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa

Command line Args:
    user (str): the mysql username
    passwd (str): the mysql password
    db (str): the database name
    name (str): the name of the state

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
                SELECT cities.name
                FROM   cities
                    LEFT JOIN states
                            ON cities.state_id = states.id
                WHERE  states.name = %s
                ORDER  BY cities.id ASC;
                """, (name,))

    rows = cur.fetchall()

    # list of cities and separators to use for printing them
    cities = []
    separator = ', '

    for city, in rows:
        cities.append(city)

    print(separator.join(cities))

    # terminating the session
    cur.close()
    conn.close()
