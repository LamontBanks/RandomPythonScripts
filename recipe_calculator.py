import pprint
import random

from recipe import Recipe

# Generate my ingredients
my_ingredients = []
num_my_ingredients = random.randint(1, 2)
for i in range(num_my_ingredients):
    while True:
        random_food = Recipe._foods[random.randint(0, len(Recipe._foods) - 1)]

        if random_food not in my_ingredients:
            my_ingredients.append(random_food)
            break
my_ingredients = sorted(my_ingredients)

# Generate recipes, try to include some of my ingredients
all_recipes = []
for i in range(50):
    all_recipes.append(Recipe(f"Meal {i}", preferred_ingredients=my_ingredients))

# Determine the recipes
full_recipes = []
close_enough_recipes = []
close_enough_range = 1

for recipe in all_recipes:
    print(recipe)

    # If we have at least a subset of the required ingredients
    # save both the exact-match and close enough recipes
    num_ingredients_missing = len(set(recipe.ingredients).difference(set(my_ingredients)))
    num_ingredients_possessed = len(set(recipe.ingredients).intersection(set(my_ingredients)))

    if num_ingredients_missing == 0:
        full_recipes.append(recipe)
    if num_ingredients_possessed >= 1 and num_ingredients_missing <= close_enough_range:
        if recipe not in full_recipes:
            close_enough_recipes.append(recipe)


print("My Ingredients:")
pprint.pprint(my_ingredients)


# for ingredient in my_ingredients:
#     for recipe in all_recipes:
#         if ingredient in recipe.ingredients:
#             print(f"- {ingredient} is in {recipe.name}, which has {len(recipe.ingredients)} ingredients")
#     print("")

print("Full Recipes:")
pprint.pprint(full_recipes)

print(f"Close Enough (only 1-{close_enough_range} extra ingredient(s)):")
pprint.pprint(close_enough_recipes)