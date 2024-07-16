class Graph:
    def __init__(self):
        # Dictionary to store the graph data using adjacency list
        self.graph = {}  

    def add_user(self, user_id, name):
        """Add a user (vertex) to the graph."""
        if user_id not in self.graph:
            self.graph[user_id] = {
                "name": name,
                "friends": set()
            }
        else:
            print(f"User {user_id} already exists in the graph.")


    def add_friendship(self, user_id1, user_id2):
        """Add a friendship (edge) between two users."""
        if user_id1 in self.graph and user_id2 in self.graph:
            self.graph[user_id1]["friends"].add(user_id2)
            self.graph[user_id2]["friends"].add(user_id1)
        else:
            print(f"One or both users ({user_id1}, {user_id2}) do not exist in the graph.")
