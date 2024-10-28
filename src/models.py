from typing import List
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Text, String, ForeignKey


class Base(DeclarativeBase):
    pass


class Recipe(Base):
    """
    Класс, описывающий рецепты
    """

    __tablename__ = "recipe"

    id: Mapped[int] = mapped_column(primary_key=True)
    recipe_name: Mapped[str] = mapped_column(String(100))
    cooking_time: Mapped[int] = mapped_column(default=5)
    views: Mapped[int] = mapped_column(default=0)
    recipe_description: Mapped[str] = mapped_column(
        Text, default="Здесь могла бы быть ваша реклама."
    )

    used_ingredients: Mapped[List["Ingredient"]] = relationship(
        back_populates="used_in_recipe", secondary="ingredients_in_recipe"
    )

    def __repr__(self):
        return f"Recipe(id={self.id}, name={self.recipe_name})"


class Ingredient(Base):
    """
    Класс, описывающий ингредиенты, входящие в рецепт
    """

    __tablename__ = "ingredient"

    id: Mapped[int] = mapped_column(primary_key=True)
    ingredient_name: Mapped[str] = mapped_column(String(100))
    ingredient_description: Mapped[str | None]

    used_in_recipe: Mapped[List["Recipe"]] = relationship(
        back_populates="used_ingredients", secondary="ingredients_in_recipe"
    )

    def __repr__(self):
        return f"Recipe(id={self.id}, name={self.ingredient_name})"


class IngredientsInRecipe(Base):
    """
    Класс, описывающий связь рецептов, ингредиентов и их количества
    """

    __tablename__ = "ingredients_in_recipe"

    recipe_id: Mapped[int] = mapped_column(
        ForeignKey("recipe.id", ondelete="CASCADE"), primary_key=True
    )
    ingredient_id: Mapped[int] = mapped_column(
        ForeignKey("ingredient.id", ondelete="CASCADE"), primary_key=True
    )
    quantity: Mapped[str | None] = mapped_column(String(100))

    def __repr__(self):
        return (
            f"IngredientsInRecipe(recipe_id={self.recipe_id}, "
            f"ingredient_id={self.ingredient_id}, quantity={self.quantity})"
        )