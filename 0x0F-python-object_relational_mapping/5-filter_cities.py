#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities of
that state, using the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    curr = conn.cursor()
    curr.execute("""
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """, (argv[4], ))
    print(", ".join(map(lambda a: a[0], curr.fetchall())))
    curr.close()
    conn.close()
