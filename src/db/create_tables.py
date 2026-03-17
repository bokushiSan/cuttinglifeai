from src.db.database import engine, Base
from sqlalchemy.schema import CreateSchema
# from src.db.models.papers import Papers
# from src.db.models.coatings import Coatings  # раскомментируй, когда нужно
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_tables():
    """
    Создание схемы и таблиц.
    """
    with engine.connect() as conn:
        if not conn.dialect.has_schema(conn, 'data'):
            conn.execute(CreateSchema('data'))
            conn.commit()

    logger.info('Создание всех таблиц...')
    Base.metadata.create_all(bind=engine)
    logger.info('Все таблицы успешно созданы или уже существуют!')

if __name__ == '__main__':
    create_tables()
