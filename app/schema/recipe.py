from pydantic import BaseModel, HttpUrl, Field

from typing import Sequence


class Recipe(BaseModel):
    id: int
    label: str
    source: str
    url: HttpUrl


class RecipeSearchResults(BaseModel):
    results: Sequence[Recipe]


class RecipeCreate(BaseModel):
    label: str = Field(example='Meat Ball')
    source: str = Field(example='Dont Starve Together')
    url: HttpUrl = Field(example='https://gg.com')
    submitter_id: int = Field(example='1')


