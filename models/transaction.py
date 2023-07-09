from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ext.database import Base


class Transaction(Base):
    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(
        'User',
        foreign_keys=[user_id],
        backref='transaction',
        cascade='all,delete',
        uselist=False,
    )
    amount = Column(Integer)
    order_id = Column(Integer)
    qty = Column(Integer)
    payment_id = Column(Integer)
    status = Column(String)
    product_id = Column(Integer)
    affiliate = Column(String, nullable=True)
    affiliate_quota = Column(Integer, nullable=True)


class Payment(Base):
    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(
        'User',
        foreign_keys=[user_id],
        backref='payment',
        cascade='all,delete',
        uselist=False,
    )
    amount = Column(Integer)
    token = Column(String(25), nullable=True)
    gateway_id = Column(Integer)
    status = Column(String)
    authorization = Column(String, nullable=True)
    payment_method = Column(String)
    payment_gateway = Column(String)
    installments = Column(Integer, default=1)
    processed = Column(
        Boolean,
        default=False,
        server_default='0',
        nullable=False,
    )
    processed_at = Column(DateTime, nullable=True)


class CreditCardFeeConfig(Base):
    id = Column(Integer, nullable=False, primary_key=True)
    min_installment_with_fee = Column(Integer)
    mx_installments = Column(Integer)
    fee = Column(Numeric)
    active_date = Column(
        DateTime,
        default=func.now(),
        server_default=func.now(),
    )
