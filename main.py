class UserNotFoundError(Exception):
    def __init__(self, username):
        self.username = username
        super().__init__(f"User not found: {username}")
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
class UserDatabase:
    def __init__(self):
        self.users = {
            'john': User('john', 'john@example.com'),
            'jane': User('jane', 'jane@example.com'),
            'alex': User('alex', 'alex@example.com')
        }
    def get_user(self, username):
        user = self.users.get(username)
        if not user:
            raise UserNotFoundError(username)
        return user
user_database = UserDatabase()
try:
    user = user_database.get_user('john')
    print(user.username, user.email)
except UserNotFoundError as e:
    print(e)
try:
    user = user_database.get_user('mary')
    print(user.username, user.email)
except UserNotFoundError as e:
    print(e)
