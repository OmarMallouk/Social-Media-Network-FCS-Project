class User:
    def __init__(self, user_id, name, email=None, age=None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.age = age
        #set to store the friends
        self.friends = set()

    def add_friend(self, friend_id):
        self.friends.add(friend_id)

    def remove_friend(self, friend_id):
        self.friends.discard(friend_id)

    def get_friends(self):
        return list(self.friends)

    # A method to return the user info as a string
    def __repr__(self):
        return (f"User(user_id={self.user_id}, name={self.name}, email={self.email}, "
                f"age={self.age}, friends={list(self.friends)})")


class Users:
    def __init__(self):
        
        # Created a dictionary to store the users(the key is user_id, value is the user)
        self.users = {}

     # method to add a user 
    def add_user(self, user_id, name, email=None, age=None):
        if user_id not in self.users:
            self.users[user_id] = User(user_id, name, email, age)
        else:
            print(f"User {user_id} already exists.")