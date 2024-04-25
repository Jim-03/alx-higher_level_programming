#!/usr/bin/python3
""" Module that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa. """
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
            user=username,
            host="localhost",
            passwd=password,
            db=db_name
            )

    my_cursor = db.cursor()
    sorted_result = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    my_cursor.execute(sorted_result)

    states = my_cursor.fetchall()

    for state in states:
        print(state)

    my_cursor.close()
    db.close()
