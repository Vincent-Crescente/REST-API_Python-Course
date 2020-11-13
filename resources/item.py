from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Every item needs a store id.")

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exits".format(name)}, 400
        # checks for price
        data = Item.parser.parse_args()

        # or item = ItemModel(name, data['price'], data['store_id'])
        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        # Pep 8 doesn't like bare exceptions they want 'except KeyError' or something.
        except:
            return {'message': "An error occurred inserting the item."}, 500  # internal server error.

        # always return JSON
        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': "Item deleted"}

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            # this means we are updating, changing price if there is a change.
            item.price = data['price']

        item.save_to_db()
        return item.json()



class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.find_all()]}
        # comprehension (above) or lambda
        #  return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}