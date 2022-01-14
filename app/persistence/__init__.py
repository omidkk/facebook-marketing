import logging

from sqlalchemy.sql import text

_log = logging.getLogger(__name__)


def init_db(db):
    _log.info("start initial the database!")
    engine = db.get_engine()
    with engine.connect() as con:
        try:
            trans = con.begin()
            file = open("sql/init_database.sql")
            query = text(file.read())
            con.execute(query)
            trans.commit()
            _log.info("database initialized")
        except Exception as e:
            _log.info("error on running init database!")
            _log.warning(e)
            trans.rollback()
