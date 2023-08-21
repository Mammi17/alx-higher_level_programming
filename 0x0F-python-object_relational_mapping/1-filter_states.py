#!/usr/bin/python3
"""lists all states with a name starting with N"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    curr = conn.cursor()
    curr.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_row = curr.fetchall()
    for r in query_row:
        if r[1].startswith("N"):
            print(r)
    curr.close()
    conn.close()
