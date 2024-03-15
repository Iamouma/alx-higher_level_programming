#!/usr/bin/python3
"""
Lists all cities of the state using the databse hbtn_0e_4_usa.
Take in 4 command line arguments mysql username, mysql password,
database name and state name (SQL injection free!)
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
    )

    cur = db.cursor()

    cur.execute(
            """SELECT * FROM cities
            INNER JOIN states
            ON cities.state_id = states.id
            ORDER BY cities.id"""
    )

    print(", ".join([city[2]
                     for city in cur.fetchall()
                     if city[4] == argv[4]]))

    cur.close()
    db.close()
