from flask import Flask, g
from app.app_factory import create_app
from app.db_connect import close_db, get_db

app = create_app()
app.secret_key = 'your-secret'  # Replace with an environment variable

# Register Blueprints
from app.blueprints.sales import sales
app.register_blueprint(sales)  # Register the 'sales' blueprint

# Import existing routes
from app import routes

@app.before_request
def before_request():
    g.db = get_db()

# Setup database connection teardown
@app.teardown_appcontext
def teardown_db(exception=None):
    close_db(exception)
