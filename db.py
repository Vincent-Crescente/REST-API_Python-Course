from flask_sqlalchemy import SQLAlchemy

# Object "SQL ALchemy", a thing that will link to our flask app and
# look at all the objects we tell it to.
# Allows to map those objects to rows in the database.
# ex. An itemModel object has a column called 'name' and a column called 'price'
# Alchemy helps put the above object into the database.

# ******* Sql Alchemy is made to change an object into a insertable row
# in our db. That's it.

db = SQLAlchemy()

