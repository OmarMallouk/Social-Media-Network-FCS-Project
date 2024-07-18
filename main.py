from tkinter import Tk
from classesData.gui import SocialNetworkApp

def main():
    root = Tk()
    app = SocialNetworkApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()