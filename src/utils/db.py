from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from config.setting import URIDB

engine = create_engine(URIDB)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# metodo alternativo
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

db: Session = SessionLocal()
