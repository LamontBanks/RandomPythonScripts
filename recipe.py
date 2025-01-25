import random

class Recipe:
    _foods = [
        'almonds', 'anchovies', 'apple', 'apple cider', 'artichoke', 'arugula', 'asparagus', 'avocado',
        'basil', 'beets', 'belgian endive', 'bell pepper', 'black pepper', 'black raspberries', 'black rice', 'black tea', 'blackberries', 'blueberries', 'bok choy', 'broad bean', 'broccoli', 'brown rice', 'brussel sprouts',
        'cabbage', 'cactus pear', 'cantaloupe', 'capers', 'cardamom', 'carrot juice', 'carrots', 'cashews', 'cauliflower', 'celery', 'chard', 'cherries', 'chestnut', 'chicken dark meat', 'chickpeas', 'chicory', 'chinese chives', 'chocolate', 'cilantro', 'cinnamon', 'clementines', 'cloves', 'cocoa powder', 'coconut', 'coffee', 'collard greens', 'cranberries', 'currants', 'cuttlefish', 
        'edamame', 'eggplant', 'escarole', 
        'fava beans', 'fennel', 'fennel seed', 'flaxseed', 'flounder', 
        'galangal', 'garlic', 'ginger', 'ginseng', 'goose', 'grapefruit', 'green beans', 'green tea', 
        'haddock', 'halibut', 'hard cheese', 'hazelnuts', 'herring', 'honey', 
        'kale', 'kiwi', 'kohlrabi', 'kumquat', 
        'lavender', 'lemon', 'lentils', 'lettuce', 'licorice root', 'lima beans', 'lime', 'lingonberry', 
        'mackerel', 'mandarin oranges', 'mango', 'maple syrup', 'mint', 'miso', 'mussels', 'mustard greens', 
        'natto', 'nectarines', 'nutmeg', 
        'oats', 'olive oil', 'olive paste', 'olives', 'onion', 'orange', 'orange juice', 'oregano', 'oysters', 
        'papaya', 'parsley', 'parsnips', 'peach', 'peanuts', 'pears', 'peas', 'pecans', 'peppermint', 'persimmon', 'pine nuts', 'pistachios', 'plums', 'pomegranate', 'poppy seed', 'pumpkin', 'pumpkin seed', 
        'quinoa', 
        'radishes', 'raspberries', 'red grapes', 'red wine', 'red wine vinegar', 'rosemary', 
        'sage', 'salmon', 'salsify', 'sardines', 'scallions', 'sea cucumber', 'seaweed', 'sesame oil', 'sesame seeds', 'shallots', 'shrimp and prawn', 'soy milk', 'soy sauce', 'soybean sprouts', 'spinach', 'squid', 'squid ink', 'strawberries', 'string beans', 'sunflower seed', 'sweet potato', 'sword jackbean', 
        'tangelos', 'tangerines', 'tarragon', 'thistle', 'thyme', 'tofu', 'tomato', 'tomato sauce', 'trout', 'tuna', 'turkey dark meat', 'turmeric', 'turnip', 'vanilla extract', 
        'walnuts', 'watercress', 'wheat', 'white wine', 'whole grains', 'winter squash', 
        'yoghurt', 
        'zucchini']

    def __init__(self, name, preferred_ingredients=[]):
        self.name = name

        # Create recipe with random ingredients + perferred
        self.ingredients = []
        
        self.num_ingredients = random.randint(1, 7)

        for i in range(self.num_ingredients):
            while True:

                # Choose from random foods or preferred (if any)

                # Purposefully randomly choose foods *beyond* the index of preferred_ingredients
                # If out of index, choose a random ingredient instead
                f = random.randint(0, len(preferred_ingredients) * 5)
                if f < len(preferred_ingredients):
                    random_food = preferred_ingredients[f]
                else:
                    random_food = self._foods[random.randint(0, len(self._foods) - 1)]

                if random_food not in self.ingredients:
                    self.ingredients.append(random_food)
                    break

        self.ingredients = sorted(self.ingredients)

    def __repr__(self):
        return f"{self.name} - {self.ingredients}"
    
    def __eq__(self, other):
        return self.ingredients == other.ingredients
        