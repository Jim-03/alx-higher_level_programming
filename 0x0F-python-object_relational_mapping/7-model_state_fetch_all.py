#!/usr/bin/python3
"""Script to list all State objects from the hbtn_0e_6_usa database."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import urllib.parse

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    details = (
            "mysql+mysqldb://{username}:{password}@"
            "localhost:3306/{database}"
            ).format(username=username,
                     password=urllib.parse.quote_plus(password),
                     database=database
                     )
    engine = create_engine(details, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id.asc()).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
