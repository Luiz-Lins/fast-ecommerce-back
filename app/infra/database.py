from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker

from config import settings


def get_engine():
    SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

    return create_engine(
        SQLALCHEMY_DATABASE_URL,
        pool_size=10,
        max_overflow=0,
    )


def get_session():
    _engine = get_engine()
    return sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=_engine,
    )


@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
