from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class SaleItemBase(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)


class SaleItemCreate(SaleItemBase):
    pass


class SaleItemResponse(SaleItemBase):
    sale_item_id: int
    sale_id: int
    unit_price: Decimal
    subtotal: Decimal | None = None

    model_config = ConfigDict(from_attributes=True)
