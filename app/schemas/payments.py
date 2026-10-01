from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field


class PaymentBase(BaseModel):
    sale_id: int
    payment_method: str
    amount_paid: Decimal = Field(..., gt=0)


class PaymentCreate(PaymentBase):
    pass


class PaymentResponse(PaymentBase):
    payment_id: int
    payment_date: datetime

    class Config:
        from_attributes = True
