from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('mysql://root:@localhost/flaskr')
db_session = scoped_session(sessionmaker(bind=engine))
