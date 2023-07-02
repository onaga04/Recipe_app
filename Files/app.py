from flask import Flask, render_template
import time

recipes = [
    {
        'title': 'Pasta Carbonara',
        'ingredients': ['spaghetti', 'bacon', 'eggs', 'cheese', 'black pepper'],
        'instructions': 'Lorem ipsum dolor sit amet...'
    },
    {
        'title': 'Chicken Parmesan',
        'ingredients': ['chicken breasts', 'breadcrumbs', 'marinara sauce', 'mozzarella cheese'],
        'instructions': 'Lorem ipsum dolor sit amet...'
    },
    # Add more recipe data as needed
]

def create_app(port):
    app = Flask(__name__)

    @app.route('/')
    def home():
        start_time = time.time()
        # Your application logic here
        # ...
        response = render_template('index.html', recipes=recipes)
        end_time = time.time()
        response_time = end_time - start_time
        # Log the response time
        app.logger.info(f"Response time for home route: {response_time} seconds")
        return response

    @app.route('/recipe/<title>')
    def recipe(title):
        start_time = time.time()
        # Your application logic here
        # ...
        # Find the recipe with the given title
        recipe = next((r for r in recipes if r['title'].lower() == title.lower()), None)

        if recipe:
            response = render_template('recipe.html', recipe=recipe)
        else:
            response = 'Recipe not found'

        end_time = time.time()
        response_time = end_time - start_time
        # Log the response time
        app.logger.info(f"Response time for recipe route: {response_time} seconds")

        return response

    return app


if __name__ == '__main__':
    # Start each server on a different port
    ports = [5000, 5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009]
    apps = [create_app(port) for port in ports]

    for i, app in enumerate(apps):
        app.run(debug=True, port=ports[i])
