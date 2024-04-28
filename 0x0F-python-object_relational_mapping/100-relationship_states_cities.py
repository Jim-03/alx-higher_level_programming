#!/usr/bin/python3
import sys
import urllib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = urllib.parse.quote_plus(sys.argv[2])
    database_name = sys.argv[3]

    details = (
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}"
        )
    engine = create_engine(details, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    session.add(new_state)
    session.add(new_city)
    session.commit()

    session.close()
