import tkinter as tk
from tkinter import messagebox
from .users import UserManager
from .graph import Graph
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class SocialNetworkApp:
    def __init__(self, root):
        self.user_manager = UserManager()
        self.social_network = Graph()
        
        self.root = root
        self.root.title("Social Network ")

        self.frame = tk.Frame(root)
        self.frame.pack()

       
         # User Section
        tk.Label(self.frame, text="Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Age").grid(row=1, column=0)
        self.age_entry = tk.Entry(self.frame)
        self.age_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Email").grid(row=2, column=0)
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.grid(row=2, column=1)

        tk.Button(self.frame, text="Add User", command=self.add_user).grid(row=3, column=0, columnspan=2)

        # Update User Section
        tk.Label(self.frame, text="Update User ID").grid(row=4, column=0)
        self.update_user_id_entry = tk.Entry(self.frame)
        self.update_user_id_entry.grid(row=4, column=1)

        tk.Label(self.frame, text="New Name").grid(row=5, column=0)
        self.new_name_entry = tk.Entry(self.frame)
        self.new_name_entry.grid(row=5, column=1)

        tk.Label(self.frame, text="New Age").grid(row=6, column=0)
        self.new_age_entry = tk.Entry(self.frame)
        self.new_age_entry.grid(row=6, column=1)

        tk.Label(self.frame, text="New Email").grid(row=7, column=0)
        self.new_email_entry = tk.Entry(self.frame)
        self.new_email_entry.grid(row=7, column=1)

        tk.Button(self.frame, text="Update User", command=self.update_user).grid(row=8, column=0, columnspan=2)

        # Friendship Section
        tk.Label(self.frame, text="User ID 1").grid(row=9, column=0)
        self.user_id1_entry = tk.Entry(self.frame)
        self.user_id1_entry.grid(row=9, column=1)

        tk.Label(self.frame, text="User ID 2").grid(row=10, column=0)
        self.user_id2_entry = tk.Entry(self.frame)
        self.user_id2_entry.grid(row=10, column=1)

        tk.Label(self.frame, text="Weight").grid(row=11, column=0)
        self.weight_entry = tk.Entry(self.frame)
        self.weight_entry.grid(row=11, column=1)

        tk.Button(self.frame, text="Add Friendship", command=self.add_friendship).grid(row=12, column=0, columnspan=2)
        
        tk.Button(self.frame, text="Remove Friendship", command=self.remove_friendship).grid(row=13, column=0, columnspan=2)

        # Display Section
        tk.Button(self.frame, text="Display Users", command=self.display_users).grid(row=14, column=0, columnspan=2)
        self.output_text = tk.Text(self.frame, height=10, width=40)
        self.output_text.grid(row=15, column=0, columnspan=2)

        # Graph Visualization Section
        tk.Button(self.frame, text="Show Network Graph", command=self.show_network_graph).grid(row=16, column=0, columnspan=2)

        # BFS and DFS Section
        tk.Label(self.frame, text="Start User ID").grid(row=17, column=0)
        self.start_user_id_entry = tk.Entry(self.frame)
        self.start_user_id_entry.grid(row=17, column=1)

        tk.Button(self.frame, text="BFS", command=self.bfs).grid(row=18, column=0)
        tk.Button(self.frame, text="DFS", command=self.dfs).grid(row=18, column=1)

        self.output_text_2 = tk.Text(self.frame, height=10, width=40)
        self.output_text_2.grid(row=19, column=0, columnspan=2)


    #
    def add_user(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        email = self.email_entry.get()
        user_id = self.user_manager.add_user(name, age, email)
        if user_id is None:
            messagebox.showerror("Error", f"User with email {email} already exists.")
        else:
            self.social_network.add_user(user_id, name)
            messagebox.showinfo("Success", f"User {name} added successfully!")
        
       
    def update_user(self):
        user_id = int(self.update_user_id_entry.get())
        new_name = self.new_name_entry.get()
        new_email = self.new_email_entry.get()
        success =  self.user_manager.update_user(user_id, name=new_name, email=new_email)
        if success:
            if new_name:
                self.social_network.update_user_name(user_id, new_name)
            messagebox.showinfo("Success", f"User {user_id} updated successfully!")
        else:
            messagebox.showerror("Error", f"Failed to update user {user_id}. Email may already exist.")

    
    def delete_user(self):
        user_id = int(self.delete_user_id_entry.get())
        if self.user_manager.delete_user(user_id):
            self.social_network.remove_user(user_id)
            messagebox.showinfo("Success", f"User {user_id} deleted successfully!")
        else:
            messagebox.showerror("Error", "User ID does not exist.")


    def add_friendship(self):
        try:
            user_id1 = int(self.user_id1_entry.get())
            user_id2 = int(self.user_id2_entry.get())
            weight = float(self.weight_entry.get())

            if not self.user_manager.get_user(user_id1):
                messagebox.showerror("Error", f"User ID {user_id1} does not exist.")
                return

            if not self.user_manager.get_user(user_id2):
                messagebox.showerror("Error", f"User ID {user_id2} does not exist.")
                return

            if user_id1 == user_id2:
                messagebox.showerror("Error", "A user cannot be friends with themselves.")
                return

            #self.user_manager.add_friend(user_id1, user_id2)
            self.social_network.add_friendship(user_id1, user_id2, weight)
            
            messagebox.showinfo("Success", f"Friendship added between User {user_id1} and User {user_id2} with weight {weight}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid user IDs.")
    



    def remove_friendship(self):
        user_id1 = int(self.user_id1_entry.get())
        user_id2 = int(self.user_id2_entry.get())
        self.social_network.remove_friendship(user_id1, user_id2)
        messagebox.showinfo("Success", f"Friendship between {user_id1} and {user_id2} removed successfully!")


    def display_users(self):
        self.output_text.delete(1.0, tk.END)
        users = self.user_manager.get_all_users()
        if not users:
            self.output_text.insert(tk.END, "No users in the network.\n")
        for user in users:
            self.output_text.insert(tk.END, f"User: {user.name} (ID: {user.id})\n")
            friends = self.social_network.get_friends(user.id)
            if friends:
                friend_names = [self.user_manager.get_user(friend_id).name for friend_id in friends]
                self.output_text.insert(tk.END, "  Friends: " + ", ".join(friend_names) + "\n")
            else:
                self.output_text.insert(tk.END, "  No friends\n")

    
    def show_network_graph(self):
        self.social_network.draw_graph()

    
    def bfs(self):
        try:
            start_user_id = int(self.start_user_id_entry.get())
            order = self.social_network.bfs(start_user_id)
            self.output_text_2.delete(1.0, tk.END)
            if not order:
                self.output_text_2.insert(tk.END, "No users found in the BFS traversal.\n")
            else:
                self.output_text_2.insert(tk.END, "BFS Order:\n")
                for user_id in order:
                    user = self.user_manager.get_user(user_id)
                    if user:
                        self.output_text_2.insert(tk.END, f"{user.name} (ID: {user.id})\n")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid start user ID.")
    

    def dfs(self):
        try:
            start_user_id = int(self.start_user_id_entry.get())
            order = self.social_network.dfs(start_user_id)
            self.output_text_2.delete(1.0, tk.END)
            if not order:
                self.output_text_2.insert(tk.END, "No users found in the DFS traversal.\n")
            else:
                self.output_text_2.insert(tk.END, "DFS Order:\n")
                for user_id in order:
                    user = self.user_manager.get_user(user_id)
                    if user:
                        self.output_text_2.insert(tk.END, f"{user.name} (ID: {user.id})\n")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid start user ID.")