from db import db


class ItemModel(db.Model):

    __tablename__ = 'items'

    # columns made for this class, put into the init parameters.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')
    # the line above lets SQL Alchemy know that the store model has
    # a primary id that will help identify itself as well as identify
    # items whose foreign key (id) matches the store.
    # **** So, now, every item model has a property store
    # that is the store which matches this store id in its id******

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    # if you look at this func in prev sections you'll see how alchemy is
    # making things shorter
    @classmethod
    def find_by_name(cls, name):
        # select * from __tablename__ where name=name LIMIT 1. 2nd name is the parameter
        # returns a item model object.
        return cls.query.filter_by(name=name).first()

    # updating or inserting is handled by this, lec 99, (upserting)
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
