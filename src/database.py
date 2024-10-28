from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy import select
from src.data_for_recipes import recipes, ingredients, ingredients_to_recipes
from src.models import Base, Recipe, Ingredient, IngredientsInRecipe

async_engine = create_async_engine("sqlite+aiosqlite:///./app.db")
async_session = async_sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


async def all_recipes():
    """
    Функция получения всех рецептов из базы данных с сортировкой
    по количеству просмотров, а если просмотры одинаковы, то по времени
    приготовления рецепта.
    - Название рецепта.
    - Время приготовления.
    - Количество просмотров.
    :return: Список рецептов.
    """
    async with async_session() as session:
        stmt = select(Recipe).order_by(-Recipe.views, Recipe.cooking_time)
        result = await session.execute(stmt)
        return result


async def detail_recipe(recipe_id: int):
    """
    Функция получения детальной информации о рецепте. Которая включает в себя:
    - id
    - Название рецепта.
    - Время приготовления.
    - Список ингредиентов.
    - Текстовое описание.
    :param recipe_id: Id рецепта, который хотим посмотреть.
    :return:
    """
    async with async_session() as session:
        result = await session.execute(
            select(Recipe).filter(Recipe.id == recipe_id)
        )

        result_2 = await session.execute(
            select(
                IngredientsInRecipe.quantity,
                Ingredient.ingredient_name,
                Ingredient.ingredient_description,
            )
            .join(
                Ingredient, Ingredient.id == IngredientsInRecipe.ingredient_id
            )
            .where(IngredientsInRecipe.recipe_id == recipe_id)
        )

        recipe = result.scalars().one()
        get_ingredients = result_2.fetchall()

        recipe.views += 1
        await session.commit()

        recipe_with_ingredients = [
            {
                "id": recipe.id,
                "recipe_name": recipe.recipe_name,
                "cooking_time": recipe.cooking_time,
                "description": recipe.recipe_description,
                "ingredients": [
                    {
                        "name": i.ingredient_name,
                        "description": i.ingredient_description,
                        "quantity": i.quantity,
                    }
                    for i in get_ingredients
                ],
            },
        ]

        return recipe_with_ingredients


async def add_data(*objs):
    """
    Функция наполнения базы данных. Вставляются объекты рецептов, ингредиентов
    или связей рецептов с ингредиентами.
    :param objs: Список объектов (Recipe, Ingredients или IngredientsInRecipe)
    :return: None
    """
    async with async_session() as session:
        async with session.begin():
            session.add_all(*objs)


async def add_recipe(new_recipe):
    """
    Функция создания нового рецепта. Принимает объект рецепта и возвращает
    полученный при его создании id
    :param new_recipe:
    :return: recipe_id
    """
    async with async_session() as session:
        async with session.begin():
            session.add(new_recipe)
            await session.commit()
            return new_recipe.id


async def create_db_and_insert_data():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    # Вставка рецептов
    await add_data(recipes)
    # Вставка ингредиентов
    await add_data(ingredients)
    # Связь рецептов с ингредиентами
    await add_data(ingredients_to_recipes)
    await async_engine.dispose()
