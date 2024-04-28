#!/usr/bin/python3
"""Prints all cities from a database."""
import sys
import urllib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    username = sys.argv[1]
    password = urllib.parse.quote_plus(sys.argv[2])
    database = sys.argv[3]

    details = (
            f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
            )

    engine = create_engine(details, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    city_data = session.query(City, State)\
            .join(State, City.state_id == State.id)\
            .order_by(State.id)

    for city, state in city_data:
        print(f"{state.name}: {city.id} {city.name}")
    session.close()
