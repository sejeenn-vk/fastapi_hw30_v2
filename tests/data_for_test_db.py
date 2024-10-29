from src.models import Ingredient, IngredientsInRecipe, Recipe

recipes = [
    Recipe(
        recipe_name="recipe_1",
        cooking_time=5,
        recipe_description="recipe_description_1",
    ),
    Recipe(
        recipe_name="recipe_2",
        cooking_time=10,
        recipe_description="recipe_description_2",
    ),
    Recipe(recipe_name="recipe_3", cooking_time=15),
]

ingredients = [
    Ingredient(
        ingredient_name="ingredient_1", ingredient_description="i_description_1"
    ),
    Ingredient(
        ingredient_name="ingredient_2", ingredient_description="i_description_2"
    ),
    Ingredient(
        ingredient_name="ingredient_3", ingredient_description="i_description_3"
    ),

]

ingredients_to_recipes = [
    IngredientsInRecipe(recipe_id=1, ingredient_id=1, quantity="quantity_1"),
    IngredientsInRecipe(recipe_id=1, ingredient_id=2, quantity="quantity_2"),
    IngredientsInRecipe(recipe_id=1, ingredient_id=3, quantity="quantity_3"),
    IngredientsInRecipe(recipe_id=2, ingredient_id=1, quantity="quantity_4"),
    IngredientsInRecipe(recipe_id=2, ingredient_id=2, quantity="quantity_5"),
    IngredientsInRecipe(recipe_id=2, ingredient_id=3, quantity="quantity_6"),
    IngredientsInRecipe(recipe_id=3, ingredient_id=1, quantity="quantity_7"),
    IngredientsInRecipe(recipe_id=3, ingredient_id=2, quantity="quantity_8"),
    IngredientsInRecipe(recipe_id=3, ingredient_id=3, quantity="quantity_9"),
]
