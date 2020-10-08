from werkzeug.security import safe_str_cmp
from resources.user import UserModel
# *****
# Essentially, we have this mapping here,
# which lets us immediately find
# the user that we're looking for,
# just by knowing its username
# or immediately find the user that we're looking for
# just by knowing its user ID.


## ______________Functions______________##

def authenticate(username, password):
    # if no user found return none
    user = UserModel.find_by_username(username)
    # safer way of comparing strings, taking care of any encoding problems
    if user and safe_str_cmp(user.password, password):
        return user

# will receive a JWT token
# taken straight from the Flask JWT documentation
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
