from flask import Flask, render_template
import time

app1 = Flask(__name__)
app2 = Flask(__name__)
app3 = Flask(__name__)
app4 = Flask(__name__)
app5 = Flask(__name__)
app6 = Flask(__name__)
app7 = Flask(__name__)
app8 = Flask(__name__)
app9 = Flask(__name__)
app10 = Flask(__name__)


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

@app1.route('/')
@app2.route('/')
@app3.route('/')
@app4.route('/')
@app5.route('/')
@app6.route('/')
@app7.route('/')
@app8.route('/')
@app9.route('/')
@app10.route('/')
def home():
    start_time = time.time()
    # Your application logic here
    # ...
    return render_template('index.html', recipes=recipes)
    response = render_template('index.html', recipes=recipes)
    end_time = time.time()
    response_time = end_time - start_time
    # Log the response time
    app.logger.info(f"Response time for home route: {response_time} seconds")
    return response
    
@app1.route('/recipe/<title>')
@app2.route('/recipe/<title>')
@app3.route('/recipe/<title>')
@app4.route('/recipe/<title>')
@app5.route('/recipe/<title>')
@app6.route('/recipe/<title>')
@app7.route('/recipe/<title>')
@app8.route('/recipe/<title>')
@app9.route('/recipe/<title>')
@app10.route('/recipe/<title>')
def recipe(title):
    # Find the recipe with the given title
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

if __name__ == '__main__':
    app1.run(debug=True, port=5000)
    app2.run(debug=True, port=5001)
    app3.run(debug=True, port=5001)
    app4.run(debug=True, port=5001)
    app5.run(debug=True, port=5001)
    app6.run(debug=True, port=5001)
    app7.run(debug=True, port=5001)
    app8.run(debug=True, port=5001)
    app9.run(debug=True, port=5001)
    app10.run(debug=True, port=5001)


