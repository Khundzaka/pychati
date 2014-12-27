__author__ = 'USER'

from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
Base = declarative_base()


class Users(Base):
    __tablename__ = 'USERS'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(45))
    password = Column(String(45))
    email = Column(String(45))
    contacts = Column(Integer)
    is_online = Column(Boolean)



class Messages(Base):
    __tablename__ = 'MESSAGES'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date_time = Column(String(45))
    message = Column(Text)
    seen = Column(Boolean)
    chat_id = Column(Integer, ForeignKey("CHATS.id"))
    edited = Column(Boolean)
    from_id = Column(Integer)
    chat = relationship("Chats")


class Chats(Base):
    __tablename__ = 'CHATS'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Integer)


class ChatUsers(Base):
    __tablename__ = 'CHATUSERS'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("USERS.id"))
    chat_id = Column(Integer, ForeignKey("CHATS.id"))


class Friends(Base):
    __tablename__ = 'FRIENDS'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("USERS.id"))
    friend_id = Column(Integer, ForeignKey("USERS.id"))
    accepted = Column(Boolean)

'''
engine = create_engine('mysql+pymysql://root:1234@localhost:3306/sqlalch')
sess = sessionmaker()
sess.configure(bind=engine)
Base.metadata.create_all(engine)
'''