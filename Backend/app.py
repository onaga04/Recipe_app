from flask import Flask, request, jsonify

app = Flask(__name__)

recipes = [
    {'title': 'Pasta Carbonara', 'ingredients': ['pasta', 'eggs', 'bacon'], 'instructions': '...'},
    {'title': 'Chicken Curry', 'ingredients': ['chicken', 'curry powder', 'coconut milk'], 'instructions': '...'},
    # Add more recipes as needed
]

# Endpoint to get all recipes
@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    return jsonify(recipes)

# Endpoint to search for recipes
@app.route('/api/recipes/search', methods=['GET'])
def search_recipes():
    recipe_title = request.args.get('title')
    matching_recipes = [recipe for recipe in recipes if recipe_title.lower() in recipe['title'].lower()]
    return jsonify(matching_recipes)

# Endpoint to add a new recipe
@app.route('/api/recipes', methods=['POST'])
def add_recipe():
    new_recipe = request.get_json()
    recipes.append(new_recipe)
    return jsonify(new_recipe)

if __name__ == '__main__':
    app.run(debug=True)
