from tkinter import *
from tkinter import messagebox


from classesData.users import Users
from classesData.graph import Graph

def main():
    usersF= Users()
    socialG = Graph()

    usersF.add_user(1,"Omar","mr.mallouk.om@gmail.com", 27)
    usersF.add_user(2,"Mira","mira@gmail.com", 31)
    usersF.add_user(3,"Samer","sams@gmail.com", 28)
    usersF.add_user(4,"Ali","alis@gmail.com", 26)

    socialG.add_user(1,"Omar")
    socialG.add_user(2,"Mira")
    socialG.add_user(3,"Samer")

    usersF.add_friend(1,2)
    usersF.add_friend(3,4)

    socialG.add_friendship(1,2)

    #looping the users in social
    for user in socialG.get_users():
        #returning their name first and then id
        print(f"User: {user[1]} (ID: {user[0]})")
        #searching for user id friends
        friends = socialG.get_friends(user[0])
        if friends:
          #return a string with the friends 
          print("  Friends: " + ", ".join([friend[1] for friend in friends]))
        else:
         print("  No friends")


if __name__ == "__main__":
    main()