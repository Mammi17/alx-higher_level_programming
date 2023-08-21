#!/usr/bin/python3
"""akes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    curr = conn.cursor()
    query = """
SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    query = query.format(argv[4])
    curr.execute(query)
    query_row = curr.fetchall()
    for r in query_row:
        print(r)
    curr.close()
    conn.close()
