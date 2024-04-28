#!/usr/bin/python3
""" Lists all cities in a database."""
import sys
import urllib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State


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

    states = session.query(State).order_by(State.id.asc()).all()
    
    for state in states:
        for city in state.cities:
            print(f"{city.id}: {city.name} -> {state.name}")

    session.close()