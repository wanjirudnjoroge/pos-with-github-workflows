from pydantic import BaseModel, ConfigDict, EmailStr, Field


class SupplierBase(BaseModel):
    company_name: str = Field(min_length=1)
    contact_name: str | None = None
    phone_number: str | None = None
    email: EmailStr | None = None


class SupplierCreate(SupplierBase):
    pass


class SupplierResponse(SupplierBase):
    supplier_id: int

    model_config = ConfigDict(from_attributes=True)
