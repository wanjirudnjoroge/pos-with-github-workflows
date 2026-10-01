from pydantic import BaseModel, ConfigDict, Field


class UserBase(BaseModel):
    username: str
    email: str | None = None


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(UserBase):
    id: int = Field(validation_alias="user_id")
    is_active: bool = True

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    username: str | None = None
