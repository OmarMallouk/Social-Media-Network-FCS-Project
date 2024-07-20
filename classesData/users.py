from .user import User
class UserManager:
    def __init__(self):
        self.users = {}
        #to save the emails so they become unique :D
        self.emails = set()
    
     # method to add a user 
    def add_user(self, name, age, email):
        if email in self.emails:
            return None  # Indicating that the user already exists
        user = User(name, age, email)
        self.users[user.id] = user
        self.emails.add(email)
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
            if name:
                user.name = name
           
            if email:
                user.email = email
            return True
        return False
    
    def get_all_users(self):
        return list(self.users.values())
