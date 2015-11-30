from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()	


class Art(Base):
	__tablename__ = 'art'
	id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
	title = Column(String(250), nullable=False)
	art = Column(String, nullable=False)
	created = Column(Date)

engine = create_engine('sqlite:///artwork.db' , echo=True)
Base.metadata.create_all(engine)