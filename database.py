from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

# Create a sqlite engine instance
engine = create_engine("sqlite:///user_post.db")

# Create a DeclarativeMeta instance
Base = declarative_base()

# Define To Do class inheriting from Base
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    message = Column(String(256))
    createDate = Column(Date)