#!/usr/bin/python3
"""Prints state object with name passed argument."""
import sys
import urllib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = urllib.parse.quote_plus(sys.argv[2])
    database = sys.argv[3]
    name = sys.argv[4]

    details = (
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
            )

    engine = create_engine(details, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == name).first()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()
