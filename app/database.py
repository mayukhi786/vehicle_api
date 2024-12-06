from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./vehicles.db" 

engine = create_engine(DATABASE_URL) #Connects to SQLite
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #Provides database sessions
Base = declarative_base()
