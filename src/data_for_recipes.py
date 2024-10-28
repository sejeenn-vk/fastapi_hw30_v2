from src.models import Ingredient, IngredientsInRecipe, Recipe

recipes = [
    Recipe(
        recipe_name="Блины молочные",
        cooking_time=30,
        recipe_description="""
        Тесто лучше и быстрее размешается, если все продукты будут комнатной
        температуры, поэтому выньте яйца и молоко из холодильника заранее.
        Если вы не успели этого сделать, то молоко подогрейте в микроволновке,
        а яйца опустите в теплую воду.
        Хорошо помытые и обсушенные яйца вбейте в глубокую миску. Обязательно
        мойте яйца перед использованием, так как даже на кажущейся чистой
        скорлупе могут находиться вредные бактерии. Лучше всего использовать
        моющие средства для пищевых продуктов и щетку. Добавьте к яйцам сахар
        и соль. Их количество регулируйте по своему вкусу, сахар, как по мне,
        можно уменьшить.
        Перемешайте тесто. С небольшим количеством молока оно получится очень
        густым, так и надо — тесто такой консистенции легче размешать до
        однородности. Именно за счет этого в нем не будет комочков.
    """,
    ),
    Recipe(
        recipe_name="Блины овсяные",
        cooking_time=25,
        recipe_description="any description",
    ),
    Recipe(recipe_name="Блины постные", cooking_time=20),
]

ingredients = [
    Ingredient(
        ingredient_name="Мука пшеничная", ingredient_description="высший сорт"
    ),
    Ingredient(ingredient_name="Мука овсяная"),
    Ingredient(ingredient_name="Мука ржаная", ingredient_description="любая"),
    Ingredient(ingredient_name="Соль"),
    Ingredient(ingredient_name="Сахар"),
    Ingredient(
        ingredient_name="Яйцо куриное", ingredient_description="0 категории"
    ),
    Ingredient(ingredient_name="Яйцо перепелиное"),
    Ingredient(ingredient_name="Масло подсолнечное"),
    Ingredient(ingredient_name="Масло сливочное"),
    Ingredient(ingredient_name="Молоко"),
    Ingredient(ingredient_name="Вода"),
]

ingredients_to_recipes = [
    IngredientsInRecipe(recipe_id=1, ingredient_id=1, quantity="3 стакана"),
    IngredientsInRecipe(
        recipe_id=1, ingredient_id=10, quantity="500 миллилитров"
    ),
    IngredientsInRecipe(
        recipe_id=1, ingredient_id=4, quantity="1/2 чайных ложки"
    ),
    IngredientsInRecipe(
        recipe_id=1, ingredient_id=5, quantity="2 чайных ложки"
    ),
    IngredientsInRecipe(
        recipe_id=1, ingredient_id=8, quantity="50 миллилитров"
    ),
    IngredientsInRecipe(recipe_id=1, ingredient_id=7, quantity="2 штуки"),
    IngredientsInRecipe(recipe_id=2, ingredient_id=2, quantity="4 стакана"),
    IngredientsInRecipe(recipe_id=2, ingredient_id=10, quantity="1 литр"),
    IngredientsInRecipe(
        recipe_id=2, ingredient_id=4, quantity="1/2 чайной ложки"
    ),
    IngredientsInRecipe(
        recipe_id=2, ingredient_id=5, quantity="2 чайных ложки"
    ),
    IngredientsInRecipe(recipe_id=2, ingredient_id=9, quantity="100 грамм"),
    IngredientsInRecipe(recipe_id=3, ingredient_id=3, quantity="5 стаканов"),
    IngredientsInRecipe(
        recipe_id=3, ingredient_id=11, quantity="700 миллилитров"
    ),
    IngredientsInRecipe(
        recipe_id=3, ingredient_id=4, quantity="1/2 чайной ложки"
    ),
    IngredientsInRecipe(
        recipe_id=3, ingredient_id=5, quantity="1 чайная ложка"
    ),
    IngredientsInRecipe(
        recipe_id=3, ingredient_id=8, quantity="3 столовых ложки"
    ),
]
