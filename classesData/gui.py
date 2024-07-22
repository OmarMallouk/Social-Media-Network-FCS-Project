import tkinter as tk
from tkinter import messagebox, Toplevel
import customtkinter as ctk
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

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.frame = ctk.CTkFrame(root)
        self.frame.pack(pady=20, padx=20)

       
         # User Section
        ctk.CTkLabel(self.frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ctk.CTkEntry(self.frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ctk.CTkLabel(self.frame, text="Age").grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = ctk.CTkEntry(self.frame)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        ctk.CTkLabel(self.frame, text="Email").grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = ctk.CTkEntry(self.frame)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        ctk.CTkButton(self.frame, text="Add User", command=self.add_user).grid(row=3, column=0, columnspan=2, pady=5)

        ctk.CTkLabel(self.frame, text="Update User ID").grid(row=4, column=0, padx=5, pady=5)
        self.update_user_id_entry = ctk.CTkEntry(self.frame)
        self.update_user_id_entry.grid(row=4, column=1, padx=5, pady=5)

        ctk.CTkLabel(self.frame, text="New Name").grid(row=5, column=0, padx=5, pady=5)
        self.new_name_entry = ctk.CTkEntry(self.frame)
        self.new_name_entry.grid(row=5, column=1, padx=5, pady=5)

        ctk.CTkLabel(self.frame, text="New Email").grid(row=6, column=0, padx=5, pady=5)
        self.new_email_entry = ctk.CTkEntry(self.frame)
        self.new_email_entry.grid(row=6, column=1, padx=5, pady=5)

        ctk.CTkButton(self.frame, text="Update User", command=self.update_user).grid(row=7, column=0, columnspan=2, pady=5)

        ctk.CTkLabel(self.frame, text="Delete User ID").grid(row=8, column=0, padx=5, pady=5)
        self.delete_user_id_entry = ctk.CTkEntry(self.frame)
        self.delete_user_id_entry.grid(row=8, column=1, padx=5, pady=5)

        ctk.CTkButton(self.frame, text="Delete User", command=self.delete_user).grid(row=9, column=0, columnspan=2, pady=5)

        # Friendship Section
        ctk.CTkLabel(self.frame, text="User ID 1").grid(row=10, column=0)
        self.user_id1_entry = ctk.CTkEntry(self.frame)
        self.user_id1_entry.grid(row=10, column=1)

        ctk.CTkLabel(self.frame, text="User ID 2").grid(row=11, column=0)
        self.user_id2_entry = ctk.CTkEntry(self.frame)
        self.user_id2_entry.grid(row=11, column=1)

        ctk.CTkLabel(self.frame, text="Weight").grid(row=12, column=0)
        self.weight_entry = ctk.CTkEntry(self.frame)
        self.weight_entry.grid(row=12, column=1)

        ctk.CTkButton(self.frame, text="Add Friendship", command=self.add_friendship).grid(row=13, column=0, columnspan=2)

        ctk.CTkButton(self.frame, text="Remove Friendship", command=self.remove_friendship).grid(row=14, column=0, columnspan=2)

        # Display Section
        ctk.CTkButton(self.frame, text="Display Users", command=self.display_users).grid(row=15, column=0, columnspan=2)
        self.output_text = tk.Text(self.frame, height=10, width=50)
        self.output_text.grid(row=16, column=0, columnspan=2, pady=5)

        # Sorting Section
        ctk.CTkButton(self.frame, text="Sort Users by Name", command=self.sort_users_by_name).grid(row=17, column=0, columnspan=2, pady=5)

        # Graph Visualization Section
        ctk.CTkButton(self.frame, text="Show Network Graph", command=self.show_network_graph).grid(row=18, column=0, columnspan=2, pady=5)

        ctk.CTkButton(self.frame, text="Open Advanced Functions", command=self.open_advanced_window).grid(row=19, column=0, columnspan=2, pady=10)

    def open_advanced_window(self):
        self.advanced_window = ctk.CTkToplevel(self.root)
        self.advanced_window.title("Advanced Functions")

        advanced_frame = ctk.CTkFrame(self.advanced_window)
        advanced_frame.pack(pady=20, padx=20)

        ctk.CTkLabel(advanced_frame, text="Start User ID").grid(row=0, column=0, padx=5, pady=5)
        self.start_user_id_entry = ctk.CTkEntry(advanced_frame)
        self.start_user_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ctk.CTkButton(advanced_frame, text="BFS", command=self.bfs).grid(row=1, column=0, pady=5)
        ctk.CTkButton(advanced_frame, text="DFS", command=self.dfs).grid(row=1, column=1, pady=5)

        self.output_text_2 = tk.Text(advanced_frame, height=10, width=50)
        self.output_text_2.grid(row=2, column=0, columnspan=2, pady=5)

        ctk.CTkLabel(advanced_frame, text="Start User ID").grid(row=3, column=0, padx=5, pady=5)
        self.start_user_id_path_entry = ctk.CTkEntry(advanced_frame)
        self.start_user_id_path_entry.grid(row=3, column=1, padx=5, pady=5)

        ctk.CTkLabel(advanced_frame, text="End User ID").grid(row=4, column=0, padx=5, pady=5)
        self.end_user_id_path_entry = ctk.CTkEntry(advanced_frame)
        self.end_user_id_path_entry.grid(row=4, column=1, padx=5, pady=5)

        ctk.CTkButton(advanced_frame, text="Find Shortest Path", command=self.find_shortest_path).grid(row=5, column=0, columnspan=2, pady=5)
        self.output_text_3 = tk.Text(advanced_frame, height=10, width=50)
        self.output_text_3.grid(row=6, column=0, columnspan=2, pady=5)

        ctk.CTkButton(advanced_frame, text="Calculate Average Age", command=self.calculate_average_age).grid(row=7, column=0, columnspan=2, pady=5)
        self.output_text_4 = tk.Text(advanced_frame, height=10, width=50)
        self.output_text_4.grid(row=8, column=0, columnspan=2, pady=5)

        ctk.CTkLabel(advanced_frame, text="Search Name").grid(row=9, column=0, padx=5, pady=5)
        self.search_name_entry = ctk.CTkEntry(advanced_frame)
        self.search_name_entry.grid(row=9, column=1, padx=5, pady=5)
        ctk.CTkButton(advanced_frame, text="Search User", command=self.search_user).grid(row=10, column=0, columnspan=2, pady=5)

        self.binary_search_output_text = tk.Text(advanced_frame, height=5, width=50)
        self.binary_search_output_text.grid(row=11, column=0, columnspan=2, pady=5)
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
    
    def sort_users_by_name(self):
        self.user_manager.quick_sort()
        self.display_users()

    
    def show_network_graph(self):
       users = self.user_manager.get_all_users()
       for user in users:
            self.social_network.add_user(user.id, user.name)
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

    
    def find_shortest_path(self):
        try:
            start_user_id = int(self.start_user_id_path_entry.get())
            end_user_id = int(self.end_user_id_path_entry.get())
            path, distance = self.social_network.dijkstra(start_user_id, end_user_id)
            self.output_text_3.delete(1.0, tk.END)
            if path is None:
                self.output_text_3.insert(tk.END, "No path found.\n")
            else:
                self.output_text_3.insert(tk.END, f"Shortest Path (distance: {distance}):\n")
                for user_id in path:
                    user = self.user_manager.get_user(user_id)
                    if user:
                        self.output_text_3.insert(tk.END, f"{user.name} (ID: {user.id})\n")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid user IDs.")

    
    def search_user(self):
        name = self.search_name_entry.get()
        user = self.user_manager.binary_search(name)
        self.binary_search_output_text.delete(1.0, tk.END)
        if user:
            self.binary_search_output_text.insert(tk.END, f"User found: {user.name} (ID: {user.id})\n")
        else:
            self.binary_search_output_text.insert(tk.END, "User not found.\n")

    
    def calculate_average_age(self):
        average_age = self.user_manager.calculate_average_age()
        self.output_text_4.delete(1.0, tk.END)
        self.output_text_4.insert(tk.END, f"Average Age: {average_age:.2f}")