import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

def get_engine():
    url = os.getenv("DATABASE_URL", "sqlite:///./saferoute.db")
    return create_engine(url, future=True)

engine = get_engine()
Session = sessionmaker(bind=engine, future=True)
def init_db(): Base.metadata.create_all(engine)
