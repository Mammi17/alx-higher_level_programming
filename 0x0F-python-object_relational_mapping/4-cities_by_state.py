#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_us"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    curr = conn.cursor()
    curr.execute("SELECT cities.id, cities.name, states.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "ORDER BY cities.id ASC")
    query_row = curr.fetchall()
    for r in query_row:
        print(r)
    curr.close()
    conn.close()
