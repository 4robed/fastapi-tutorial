from pydantic import BaseModel, HttpUrl, Field


class RecipeBase(BaseModel):
    label: str
    source: str
    url: HttpUrl


class RecipeCreate(RecipeBase):
    label: str = Field(example='Meat Ball')
    source: str = Field(example='Dont Starve Together')
    url: HttpUrl = Field(example='https://gg.com')
    submitter_id: int = Field(example='1')


class RecipeUpdate(RecipeBase):
    label: str


# Properties shared by models stored in DB
class RecipeInDBBase(RecipeBase):
    id: int
    submitter_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Recipe(RecipeInDBBase):
    pass


# Properties stored in DB
class RecipeInDB(RecipeInDBBase):
    pass
