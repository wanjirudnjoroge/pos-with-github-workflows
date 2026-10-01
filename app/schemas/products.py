from pydantic import BaseModel, ConfigDict, Field


class ProductBase(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)
    category_id: int
    sku: str = Field(min_length=1)
    supplier_id: int | None = None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1)
    price: float | None = Field(default=None, gt=0)
    quantity: int | None = Field(default=None, ge=0)
    category_id: int | None = None
    sku: str | None = Field(default=None, min_length=1)
    supplier_id: int | None = None


class ProductResponse(ProductBase):
    id: int = Field(validation_alias="product_id")
    model_config = ConfigDict(from_attributes=True)
