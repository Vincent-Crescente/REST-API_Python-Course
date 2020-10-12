from app import app
from db import db

db.init_app(app)

# now we can create data.db without running create_tables.py
@app.before_first_request
def create_tables():
    db.create_all()