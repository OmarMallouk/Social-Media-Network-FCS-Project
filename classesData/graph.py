import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import heapq

class Graph:
    def __init__(self):
        # Dictionary to store the graph data using adjacency list
        self.adjacency_list = {}  
        self.graph = nx.DiGraph()
        

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
        self.graph.remove_node(user_id)

    
    def add_friendship(self, user_id1, user_id2, weight=1):
        self.graph.add_edge(user_id1, user_id2, weight=weight)

    
    def remove_friendship(self, user_id1, user_id2):
        if self.graph.has_edge(user_id1, user_id2):
            self.graph.remove_edge(user_id1, user_id2)


   
    def get_friends(self, user_id):
        return list(self.graph.successors(user_id))
        
    def update_user_name(self, user_id, new_name):
        if user_id in self.graph:
            self.graph.nodes[user_id]['name'] = new_name
        
    # draws the graph with vertices 
    def draw_graph(self):
        pos = nx.spring_layout(self.graph)
        labels = nx.get_node_attributes(self.graph, 'name')
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        plt.figure(figsize=(8, 6))
        nx.draw(self.graph, pos, with_labels=True, labels=labels, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold', arrows=True)
       
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.show()

    
    def bfs(self, start_user_id):
        visited = set()
        queue = deque([start_user_id])
        order = []

        while queue:
            user_id = queue.popleft()
            if user_id not in visited:
                visited.add(user_id)
                order.append(user_id)
                queue.extend(self.graph.successors(user_id))
        
        return order
    
    def dfs(self, start_user_id):
        visited = set()
        stack = [start_user_id]
        order = []

        while stack:
            user_id = stack.pop()
            if user_id not in visited:
                visited.add(user_id)
                order.append(user_id)
                stack.extend(reversed(list(self.graph.successors(user_id))))
        
        return order
    

    def dijkstra(self, start_user_id, end_user_id):
        distances = {node: float('inf') for node in self.graph.nodes}
        distances[start_user_id] = 0
        priority_queue = [(0, start_user_id)]
        previous_nodes = {node: None for node in self.graph.nodes}

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor in self.graph.successors(current_node):
                weight = self.graph.edges[current_node, neighbor]['weight']
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        path = []
        current_node = end_user_id
        while current_node is not None:
            path.append(current_node)
            current_node = previous_nodes[current_node]
        path = path[::-1]

        if distances[end_user_id] == float('inf'):
            return None, float('inf')

        return path, distances[end_user_id]