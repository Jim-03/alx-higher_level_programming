#!/usr/bin/python3
""" Module to list cities from a database."""
import sys
import MySQLdb


if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            user=user_name,
            passwd=password,
            db=database
            )

    my_cursor = db.cursor()
    query = """
        select cities.id, cities.name, states.name
        from cities
        join states on cities.state_id = states.id
        order by cities.id asc
        """
    my_cursor.execute(query)
    cities = my_cursor.fetchall()

    for city in cities:
        print(city)

    my_cursor.close()
    db.close()
