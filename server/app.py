from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Models currently in the Flatiron Cars catalog
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


# Default route: introduces the company
@app.route('/')
def index():
    return 'Welcome to Flatiron Cars'


# Model route: checks the URL variable against the catalog
@app.route('/<model>')
def get_model(model):
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    return f'No models called {model} exists in our catalog'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
