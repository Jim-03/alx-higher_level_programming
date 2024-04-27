#!/usr/bin/python3
""" Module to list first state from a database."""
import sys
import urllib.parse
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    details = f"mysql+mysqldb://{username}:\
            {urllib.parse.quote_plus(password)}@localhost:3306/{database}"
    engine = create_engine(details, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    first = session.query(State).order_by(State.id.asc()).first()

    if first:
        print(f"{first.id}: {first.name}")
    else:
        print("Nothing")
    session.close()
