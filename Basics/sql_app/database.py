from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# pip install mysql-connector-python python-dotenv
SQLALCHEMY_DATABASE_URL = "mysql://root:rosxnb$ROOT0@localhost:3306/fastapi1"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
