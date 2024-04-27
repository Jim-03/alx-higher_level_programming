#!/usr/bin/python3
""" Adds an object to database."""
import sys
import urllib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    state = session.query(State).filter(State.name == 'Louisiana').first()
    if state:
        print(f"{state.id}")
    session.close()
