import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        # Dictionary to store the graph data using adjacency list
        self.adjacency_list = {}  
        self.graph = nx.Graph()

    #adding user and plotting to the graph
    def add_user(self, user_id, name):
        """Add a user (vertex) to the graph."""
        if user_id not in self.adjacency_list:
            self.adjacency_list[user_id] = {
                "name": name,
                "friends": set()
            }
            self.graph.add_node(user_id, name=name)
        else:
            print(f"User {user_id} already exists in the graph.")

    def remove_user(self, user_id):

        """Remove a user from the graph."""

        if user_id in self.users:

            del self.users[user_id]

            for user in self.users.values():

                user["friends"].discard(user_id)

        else:

            print(f"User {user_id} does not exist in the graph.")


    def add_friendship(self, user_id1, user_id2):
        """Add a friendship (edge) between two users."""
        if user_id1 in self.adjacency_list and user_id2 in self.adjacency_list:
            self.adjacency_list[user_id1]["friends"].add(user_id2)
            self.adjacency_list[user_id2]["friends"].add(user_id1)
            self.graph.add_edge(user_id1, user_id2)
        else:
            print(f"One or both users ({user_id1}, {user_id2}) do not exist in the graph.")

    
    def remove_friendship(self, user_id1, user_id2):

        """Remove a friendship between two users."""

        if user_id1 in self.adjacency_list and user_id2 in self.adjacency_list:

            self.adjacency_list[user_id1]["friends"].discard(user_id2)

            self.adjacency_list[user_id2]["friends"].discard(user_id1)

        else:

            print(f"One or both users ({user_id1}, {user_id2}) do not exist in the graph.")


    def get_users(self):
        """Return a list of all users in the graph."""
        return [(user_id, self.adjacency_list[user_id]["name"]) for user_id in self.adjacency_list]

    def get_friends(self, user_id):
        """Return a list of friends for a given user."""
        if user_id in self.adjacency_list:
            return [(friend_id, self.adjacency_list[friend_id]["name"]) for friend_id in self.adjacency_list[user_id]["friends"]]
        else:
            print(f"User {user_id} does not exist in the graph.")
            return []
        
    # draws the graph with vertices 
    def draw_graph(self):
        pos = nx.spring_layout(self.graph)
        labels = nx.get_node_attributes(self.graph, 'name')
        nx.draw(self.graph, pos, with_labels=True, labels=labels, node_size=5000, node_color='lightblue', font_size=10, font_color='black')
        plt.show()
        
    def __repr__(self):
        """Return a string representation of the graph."""
        return f"Graph({self.graph})"