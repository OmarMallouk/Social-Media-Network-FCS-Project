
class Users:
    def __init__(self):
        
        # Created a dictionary to store the users(the key is user_id, value is the user)
        self.users = {}

     # method to add a user 
    def add_user(self, user_id, name, email=None, age=None):
        if user_id not in self.users:
            self.users[user_id] ={
                "user_id": user_id,
                "name": name,
                "email": email,
                "age": age,
                "friends": set()
            }
        else:
            print(f"User {user_id} already exists.")

    # method to get user by id
    def get_user(self, user_id):
        user = self.users.get(user_id, None)
        if user:
            user_names = {
                "user_id": user["user_id"],
                "name": user["name"],
                "email": user["email"],
                "age": user["age"],
                "friends": [self.users[friend_id]["name"] for friend_id in user["friends"]]
            }
            return user_names
        else:
            print(f"User {user_id} does not exist.")
            return None

    # method to remove a user by id
    def remove_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
        else:
            print(f"User {user_id} does not exist.")

    # implemented a method to add a friend to an existing user
    def add_friend(self, user_id, friend_id):
        user = self.get_user(user_id)
        friend = self.get_user(friend_id)
        if user and friend:
            self.users[user_id]["friends"].add(friend_id)
            self.users[friend_id]["friends"].add(user_id)
        else:
            print("One or both users do not exist.")

     #a method to remove a friend by id 
    def remove_friend(self, user_id, friend_id):
        user = self.get_user(user_id)
        friend = self.get_user(friend_id)
        if user and friend:
            self.users[user_id]["friends"].discard(friend_id)
            self.users[friend_id]["friends"].discard(user_id)
        else:
            print("One or both users do not exist.")
    
    #method to get a friend by id
    def get_friends(self, user_id):
        user = self.get_user(user_id)
        if user:
           return user["friends"]
        else:
            print(f"User {user_id} does not exist.")
            return []

    def __repr__(self):
        return f"Users(users={self.users})"

