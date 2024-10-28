from typing import List

from pydantic import BaseModel


class RecipeOut(BaseModel):
    id: int | None
    recipe_name: str
    cooking_time: int
    views: int | None

    # class Config:
    #     from_attributes = True


class Ingredients(BaseModel):
    ingredient_id: int
    quantity: str


class RecipeIn(BaseModel):
    recipe_name: str
    cooking_time: int
    recipe_description: str
    ingredients: List[Ingredients]


class Ingredient(BaseModel):
    name: str
    description: str | None
    quantity: str | None


class RecipeDetail(BaseModel):
    id: int
    recipe_name: str
    cooking_time: int
    description: str
    ingredients: List[Ingredient]