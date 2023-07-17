# pylint: disable=attribute-defined-outside-init
from __future__ import annotations
import abc
from decimal import Decimal
from typing import TypeVar
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker

from app.entities.product import ProductCart, ProductInDB
from app.cart import repository


from config import settings


Self = TypeVar('Self')


class AbstractUnitOfWork(abc.ABC):
    cart = repository.AbstractRepository

    async def get_product_by_id(self: Self, product_id: int) -> ProductCart:
        """Must return a product by id."""
        return await self._get_product_by_id(product_id=product_id)

    async def get_products(self: Self, products: list) -> ProductCart:
        """Must return a product by id."""
        return await self._get_products(products=products)

    @abc.abstractmethod
    async def _get_product_by_id(self: Self, product_id: int) -> ProductCart:
        """Must return a product by id."""
        ...

    @abc.abstractmethod
    async def _get_products(self: Self, products: list) -> list:
        """Must return a product by id."""
        ...


def get_engine() -> AsyncEngine:
    """Create a new engine."""
    return create_async_engine(
        settings.DATABASE_URI,
        pool_size=10,
        max_overflow=0,
        echo=True,
    )


def get_session() -> sessionmaker:
    """Create a new session."""
    return sessionmaker(
        bind=get_engine(),
        expire_on_commit=False,
        class_=AsyncSession,
    )


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(
        self: Self,
        session_factory: sessionmaker = get_session(),  # noqa: B008
    ) -> None:
        self.session = session_factory
        self.cart = repository.SqlAlchemyRepository(session_factory)

    async def get(self: Self) -> None:
        async with self._session() as session, session.begin():
            await session.execute('SELECT 1')

    async def _get_product_by_id(self: Self, product_id: int) -> ProductInDB:
        """Must return a product by id."""
        product_db = await self.cart.get_product_by_id(product_id=product_id)
        return ProductInDB.model_validate(product_db)

    async def _get_products(self: Self, products: list) -> list[ProductCart]:
        """Must return a products in list."""
        product_ids: list[int] = [item.product_id for item in products]
        products_db = await self.cart.get_products(products=product_ids)
        return [ProductInDB.model_validate(product) for product in products_db]


class MemoryUnitOfWork(AbstractUnitOfWork):
    async def _get_product_by_id(self: Self, product_id: int) -> ProductCart:
        """Must add product to new cart and return cart."""

        async def create_product_cart() -> ProductCart:
            return ProductCart(
                product_id=product_id,
                quantity=10,
                price=Decimal('10.00'),
            )

        return await create_product_cart()

    async def _get_products(
        self: Self,
        products: list[ProductInDB],
    ) -> list[ProductInDB]:
        """Must return a list of products."""
        _ = products

        async def return_product_list() -> list:
            return [
                ProductInDB(
                    id=1,
                    name='test_1',
                    uri='/test',
                    price=10000,
                    active=True,
                    direct_sales=False,
                    description='description 1',
                    discount=100,
                    category_id=1,
                    showcase=True,
                    show_discount=True,
                    upsell=None,
                    image_path='',
                    installments_config=1,
                    installments_list=[],
                    height=None,
                    width=None,
                    weight=None,
                    length=None,
                    diameter=None,
                    sku='sku_1',
                ),
                ProductInDB(
                    id=2,
                    name='test_2',
                    uri='/test',
                    price=20000,
                    active=True,
                    direct_sales=False,
                    description='description 1',
                    discount=0,
                    category_id=1,
                    showcase=True,
                    show_discount=True,
                    upsell=None,
                    image_path='',
                    installments_config=1,
                    installments_list=[],
                    height=None,
                    width=None,
                    weight=None,
                    length=None,
                    diameter=None,
                    sku='sku_2',
                ),
            ]

        return await return_product_list()
