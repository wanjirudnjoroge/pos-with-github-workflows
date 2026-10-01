from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from app.schemas.sale_items import SaleItemCreate, SaleItemResponse


class SaleCreate(BaseModel):
    customer_id: int | None = None
    payment_method: str = Field(default="cash", min_length=1)
    items: list[SaleItemCreate] = Field(min_length=1)


class SaleResponse(BaseModel):
    sale_id: int
    user_id: int
    customer_id: int | None = None
    payment_method: str
    created_at: datetime
    total_amount: Decimal
    sale_items: list[SaleItemResponse]
    model_config = ConfigDict(from_attributes=True)
