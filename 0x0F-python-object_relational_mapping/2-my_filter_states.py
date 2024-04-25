#!/usr/bin/python3
""" Module that displays values depending on the argument."""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=db_name
            )

    my_cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC".format(state_name)
    my_cursor.execute(query)
    results = my_cursor.fetchall()

    for state in results:
        print(state)

    my_cursor.close()
    db.close()
