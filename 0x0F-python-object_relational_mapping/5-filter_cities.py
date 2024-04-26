#!/usr/bin/python3
""" Module to list all cities based on astate."""
import sys
import MySQLdb


if __name__ == "__main__":
    name = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            user=name,
            passwd=password,
            db=database
            )

    my_cursor = db.cursor()
    query = """
    select cities.name
    from cities
    join states on cities.state_id = states.id
    where states.name like %s
    """
    my_cursor.execute(query, (state_name,))
    cities = [city[0] for city in my_cursor.fetchall()]
    print(", ".join(cities))
    my_cursor.close()
    db.close()
