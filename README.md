# RandomPythonScripts

### Random Name Generator
Generate names based on prexisting names, kind of useful useful for table/videogame character names.

### Usage
    $ python3 random_name_generator.py <txt of names>

    Ex:
    $ python3 random_name_generator.py names.txt
    
    [
        'Roda',
        'Fannaas',
        'Aalrrena',
        'Mlaaar',
        'Laeraaea',
        'Yadsenn',
        'Kaaraada',
        'Fhyeiia',
        etc...
    ]

## Dummy Recipe Calculator
Generate fake recipes, then find recipes matching our current ingredients.
Practice/scratchwork for a proper crafting calculator

## Usage
$ python3 recipe_calculator.py

    My Ingredients:
    ['mustard greens', 'shallots']
    Full Recipes:
    [Meal 6 - ['mustard greens', 'shallots'], Meal 43 - ['mustard greens']]
    Close Enough (only 1-2 extra ingredient(s)):
    [Meal 3 - ['garlic', 'lentils', 'mustard greens'],
    Meal 10 - ['avocado', 'mustard greens'],
    Meal 13 - ['kale', 'shallots', 'thistle'],
    etc.

Will likely need to run multiple times to find matches due to randomization