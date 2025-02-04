from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    description: str | None = None


class ItemRead(ItemCreate):
    id: int

    class Config:
        from_attributes = True
