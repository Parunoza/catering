# catering_server/database.py
from databases import Database
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Database connection URL
DATABASE_URL = "postgresql://postgres:catering123@localhost:5432/catering"

database = Database(DATABASE_URL)
