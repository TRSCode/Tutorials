from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# sqlite3
# SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"

# postgresql
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:VBtreat01@localhost:5432/TodoApplicationDatabase"

# mysql
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@127.0.0.1:3306/TodoApplicationDatabase"

# ------------------------------------------------------------------------------------------------

#sqlite3
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# postgresql
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# mysql
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
