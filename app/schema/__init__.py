from pydantic import BaseModel


class Recipe(BaseModel):
    id: int
    label: str
    source: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    # Docs schema example
    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }
