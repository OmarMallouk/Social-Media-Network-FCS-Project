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