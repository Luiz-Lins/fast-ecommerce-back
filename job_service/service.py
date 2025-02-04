import json

import psycopg2
import httpx
from dynaconf import settings
from loguru import logger
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from models.order import OrderStatusSteps


def get_session():
    engine = create_engine(settings.DATABASE_URL, echo=True)
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def post_order_status(url):
    response = httpx.post(url=url)
    return response


def process():
    session = get_session()
    result = session.query(OrderStatusSteps).filter_by(
        active=True, sending=False
    )
    result_list = [
        {'Order_id': row.id, 'Status': row.status} for row in result
    ]
    logger.debug(f'SETTINGS ------ {settings.API_MAIL_URL}')
    url = post_order_status(settings.API_MAIL_URL)
    return result_list


def main():
    process()


if __name__ == '__main__':
    main()
