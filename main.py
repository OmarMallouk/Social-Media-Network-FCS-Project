from tkinter import Tk
import customtkinter as ctk
from classesData.gui import SocialNetworkApp

def main():
    root = ctk.CTk()
    root.geometry("800x900")
    app = SocialNetworkApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
