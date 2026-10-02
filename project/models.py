from pydantic import BaseModel, Field


class Item(BaseModel):
    creator : str = Field(min_length=1)
    model : str = Field(min_length=1)
    price : int = Field(ge=0)
    category : str = Field(min_length=1)
