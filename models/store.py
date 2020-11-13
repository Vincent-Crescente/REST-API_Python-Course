from db import db

class StoreModel(db.Model):

    __tablename__ = 'stores'

    # columns made for this class, put into the init parameters.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    items = db.relationship('ItemModel', lazy='dynamic')
    # Store has a one to many relationship with the items with this line
    # it goes to the item model and sees the store variable
    # thus it knows these are in a relationship
    # Lec 103 "And then it goes into the item (model) and it finds that there's a store id here and then it goes, ah-ha, there's a store id in the item
    # which means that one item is related to a store. Therefore there could be more than one item
    # related to the same store.

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
                'id': self.id,
                'name': self.name,
                'items': [item.json() for item in self.items.all()]
              }

    # if you look at this func in prev sections you'l see how alchemy is
    # making things shorter
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
