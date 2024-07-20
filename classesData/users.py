from .user import User
class UserManager:
    def __init__(self):
        self.users = {}
        #to save the emails so they become unique :D
        self.emails = set()
        #to make the name unique
        self.names = set()
    
     # method to add a user 
    def add_user(self, name, age, email):
        if email in self.emails or name in self.names:
            return None  # Indicating that the user already exists
        user = User(name, age, email)
        self.users[user.id] = user
        self.emails.add(email)
        self.names.add(name)
        return user.id
    

    def get_user(self, user_id):
        return self.users.get(user_id, None)
    
    def update_user(self, user_id, name=None,  email=None):
        user = self.get_user(user_id)
        if user:
            if email and email != user.email:
                if email in self.emails:
                    return False  # Indicating that the new email already exists
                self.emails.remove(user.email)
                self.emails.add(email)
                user.email = email
            if name and name != user.name:
                if name in self.names:
                    return False  # Indicating that the new name already exists
                self.names.remove(user.name)
                self.names.add(name)
                user.name = name
            return True
        return False
    

    def delete_user(self, user_id):
        user = self.get_user(user_id)
        if user:
            self.emails.remove(user.email)
            self.names.remove(user.name)
            del self.users[user_id]
            return True
        return False

    def get_all_users(self):
        return list(self.users.values())
