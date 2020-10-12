from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.user import UserRegister
from security import authenticate, identity
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__)
# Turns off the flask sql alchemy tracker. B/c sqlalchemy itself has its own.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SQL Alchemy will read where our db is. It can be any db.. msql, postgresSql, oracle
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

# THE FILE YOU FIRST RUN WILL HAVE THE NAME MAIN.
# IF not then it has been imported from somewhere else.
if __name__ == '__main__':
    app.run(port=5000, debug=True)
