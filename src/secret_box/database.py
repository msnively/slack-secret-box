import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import config

db_path = config["database"]["path"]
db_engine_str = "sqlite:///" + db_path

engine = create_engine(db_engine_str, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)


def check_db():
    # make sure database exists before using it
    if not (os.path.exists(db_path)):
        parent_path, filename = os.path.split(db_path)
        if not os.path.exists(parent_path):
            os.makedirs(parent_path)
        init_db()

check_db()
