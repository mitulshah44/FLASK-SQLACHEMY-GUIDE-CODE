from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, backref, relationship

from config import engine

# Usefull documentation to create session with flask
# http://flask.pocoo.org/snippets/22/


Base = declarative_base()
# Session = sessionmaker(bind=engine)
# create session whenever you transaction with database
# session = Session()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(250))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '{} {}'.format(self.username, self.email)


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", backref=backref('addresses', order_by=id))

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address
