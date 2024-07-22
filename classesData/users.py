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
    

    
    def quick_sort(self):
        users_list = list(self.users.values())
        self._quick_sort_recursive(users_list, 0, len(users_list) - 1)
        self.users = {user.id: user for user in users_list}

    def _quick_sort_recursive(self, arr, low, high):
        if low < high:
            pi = self._partition(arr, low, high)
            self._quick_sort_recursive(arr, low, pi - 1)
            self._quick_sort_recursive(arr, pi + 1, high)

    def _partition(self, arr, low, high):
        pivot = arr[high].name
        i = low - 1
        for j in range(low, high):
            if arr[j].name <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    

    def get_sorted_users_by_name(self):
        return sorted(self.users.values(), key=lambda user: user.name)

    def binary_search(self, name):

        sorted_users = self.get_sorted_users_by_name()
        low, high = 0, len(sorted_users) - 1
        while low <= high:
         mid = (low + high) // 2
        if sorted_users[mid].name == name:
            return sorted_users[mid]
        elif sorted_users[mid].name < name:
            low = mid + 1
        else:
            high = mid - 1
        return None
    
    def calculate_average_age(self):
        if not self.users:
            return 0
        total_age = sum(user.age for user in self.users.values())
        average_age = total_age / len(self.users)
        return average_age