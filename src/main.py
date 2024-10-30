import uvicorn
import asyncio
from fastapi import FastAPI
from src.database import create_db_and_insert_data, all_recipes, detail_recipe, add_recipe, add_data
from src.models import Recipe, Ingredient, IngredientsInRecipe
from src.schemas import RecipeDetail, RecipeIn, RecipeOut
from src.data_for_recipes import recipes, ingredients, ingredients_to_recipes

app = FastAPI()


@app.get("/")
def main_page():
    # Главная страница
    return {"message": "Main page"}


@app.get("/create_db")
async def create_db():
    # Создание базы данных и наполнение ее какими-то данными
    await create_db_and_insert_data(recipes, ingredients, ingredients_to_recipes)
    return {'message': "База данных создана"}


@app.get("/recipes")
async def show_all_recipes():
    # показать все рецепты
    result = await all_recipes()
    data = result.scalars().all()
    return data


@app.get("/recipes/{recipe_id}")
async def get_recipe_details(recipe_id):
    # Показать детали выбранного рецепта
    recipe_with_ingredients = await detail_recipe(recipe_id)
    return recipe_with_ingredients


@app.post("/", response_model=RecipeIn)
async def add_new_recipe(recipe: RecipeIn):
    # Добавить новый рецепт
    new_recipe = Recipe(
        recipe_name=recipe.recipe_name,
        cooking_time=recipe.cooking_time,
        recipe_description=recipe.recipe_description,
    )
    ingredients = recipe.ingredients
    new_recipe_id = await add_recipe(new_recipe)
    ingredients_in_recipe = [
        IngredientsInRecipe(
            recipe_id=new_recipe_id,
            ingredient_id=i.ingredient_id,
            quantity=i.quantity,
        )
        for i in ingredients
    ]
    if new_recipe_id:
        await add_data(ingredients_in_recipe)
        return recipe


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
