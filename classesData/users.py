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
