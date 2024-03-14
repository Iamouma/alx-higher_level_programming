#!/usr/bin/python3
"""
This displays all values in the states table of the database hbtn_0e_0_usa
whose name matches that supplied as argument.
The script takes 4 arguments <mysql username> <mysql password> <database name>
and <state name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], port=3306, host="localhost",
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(sys.argv[4]))
    states = cur.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
    cur.close()
    db.close()
