from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv 
import os
 
load_dotenv()

    
DB_HOST = os.getenv("DB_HOST") 
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PORT = os.getenv("MYSQL_PORT")
 
# With locally
SQLALCHEMY_DATABASE_URL = "mysql://{USER}:{PASS}@{HOST}:{PORT}/{DB_NAME}".format(
    HOST=DB_HOST,
    DB_NAME=MYSQL_DATABASE,
    PASS=MYSQL_PASSWORD,
    USER=MYSQL_USER,
    PORT=MYSQL_PORT
)


print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)


meta= MetaData()

conection=engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
