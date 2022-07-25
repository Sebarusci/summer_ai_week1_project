# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
from re import A
import json

class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                # you can save objects of people on the network in this list
        self.user = ""
        self.pwd = ""
       
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def  create_account(self):
        #Function that creates an account and a password.
        while True:
            username = input("Type your new username: ")
            if username in self.list_of_people:
                print('Username already in use!')
            else:
                break
        password = input("Type your new password: ")
        print("Creating...")
        self.list_of_people.append(username)
        self.pwd = password
        self.user = username

class Person():
    def __init__(self, name, password):
        self.username = name
        self.password = password
        self.friendlist = []
        self.person_object = None
        self.blocked_object = None
        self.block_list = []
        self.user_messages = []
        
    def edit_user(self):
        print("")
        print("Old username: ", self.username)
        new_username = input("Type new username: ")
        self.username = new_username

    def edit_pwd(self):
        print("")
        print("Old password: ", self.password)
        new_password = input("Type new password: ")
        self.password = new_password
    
    def add_friend(self, person_object):
        #implement adding friend. Hint add to self.friendlist
        self.friendlist.append(person_object)
        
    def view_friend(self):
        # Views friend list
        print("")
        print("Friend list:")
        print("=============")
        print(self.friendlist)
        print("=============")

    def block_friend(self, blocked_object):
        # Blocks a friend and removes the person from the friend list, adding it to the block list.
        if blocked_object in self.friendlist:
            self.friendlist.remove(blocked_object)
            self.block_list.append(blocked_object)
        
    def blocked_list(self):
        # Shows the block list
        print("")
        print("Blocked friends:")
        print("=============")
        print(self.block_list)
        print("=============")

    def unblock(self, unblocked):
        # Removes a friend from the block list and adds it back again into the friend list.
        if unblocked in self.block_list:
            self.block_list.remove(unblocked)
            self.friendlist.append(unblocked)
    
    def send_message(self, message, person):
        #implement sending message to friend here
        print("")
        print(message)
        print("")
        msg_1 = "From: You | To: "+ str(person) + "| message:" + str(message)
        self.user_messages.append(msg_1)
        print("message sent!")

    def view_message(self):
        print(self.user_messages)
