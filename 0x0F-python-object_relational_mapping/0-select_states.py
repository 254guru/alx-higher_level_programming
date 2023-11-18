#!/usr/bin/python3
"""
list all states in a database
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    Access the database and get the states
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)
