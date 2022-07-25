#Various import Statements can go here
from turtle import back
from  social_network_classes import SocialNetwork,Person
import social_network_ui

#Create instance of main social network object
ai_social_network = SocialNetwork()

# Create account variable to know wether user is signed in.
account = None

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("      ____  _____   ______          ___   _ ")
    print("     |  _ \|  __ \ / __ \ \        / / \ | |")
    print("     | |_) | |__) | |  | \ \  /\  / /|  \| |")
    print("     |  _ <|  _  /| |  | |\ \/  \/ / | . ` |")
    print("     | |_) | | \ \| |__| | \  /\  /  | |\  |")
    print("     |____/|_|  \_\\____/   \/  \/   |_| \_|")  
    print("")                              
    print("               The Brown Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            # Creates and account and creates an instance in the Person class.
            ai_social_network.create_account()
            username = ai_social_network.user
            password = ai_social_network.pwd
            account = Person(username, password)

        elif choice == "2":
            #Checks if user has an account to access its settings.
            if account == None:
                print("")
                print("Cant access functions. Account not yet created.")
            elif account != None:
                while True:
                    #Account Info
                    print("")
                    print("Username:", account.username)
                    print("Password:", account.password)
                    #Handle inner menu here
                    inner_menu_choice = social_network_ui.manageAccountMenu()
                    # Edits user account
                    if inner_menu_choice == "1":
                        choice_2 = social_network_ui.editDetail()
                        if choice_2 == "1":
                            account.edit_user()
                        elif choice_2 == "2":
                            account.edit_pwd()
                        elif choice_2 == "3":
                            inner_menu_choice = social_network_ui.manageAccountMenu()
                        else:
                            print("Your input is invalid. Try Again!")
                            choice_2 = social_network_ui.editDetail()
                    #Add a friend option
                    elif inner_menu_choice == "2":
                        print("")
                        a = input("Friend's username: ")
                        account.add_friend(a)
                        if a in account.friendlist:
                            print("Friend already added.")
                        else:
                            print("Friend added!")
                            ai_social_network.list_of_people.append(a)
                        inner_menu_choice = social_network_ui.manageAccountMenu()
                    # View friend list
                    elif inner_menu_choice == "3":
                        while True:
                            account.view_friend()
                            out = input("<-Go back? (y/n): ")
                            if out == "y":
                                break
                            elif out == "n":
                                pass
                            else:
                                print("Your input is invalid. Try Again!")
                    # Block a friend
                    elif inner_menu_choice == "4":
                        print("")
                        print(account.friendlist)
                        print("")
                        blocked = input("Which friend would you like to block: ")
                        if blocked in account.friendlist:
                            account.block_friend(blocked)
                            print("Friend blocked. You will no longer be able to receive or send messages from this person.")
                        else:
                            print("Friend doesn't exist.")
                        inner_menu_choice = social_network_ui.manageAccountMenu()
                    # View blocked friends
                    elif inner_menu_choice == "5":
                        while True:
                            account.blocked_list()
                            out = input("<-Go back? (y/n): ")
                            if out == "y":
                                break
                            elif out == "n":
                                pass
                            else:
                                print("Your input is invalid. Try Again!")
                    # Unblock friend
                    elif inner_menu_choice == "6":
                        print("")
                        account.blocked_list()
                        Unblock = input("Which friend would you like to unblock: ")
                        account.unblock(Unblock)
                        if Unblock not in account.block_list:
                            print("Blocked friend not found")
                        else:
                            ai_social_network.list_of_people.append(blocked)
                    # Send message
                    elif inner_menu_choice == "7":
                        print(account.friendlist)
                        print("")
                        receiver = input("Who would you like to message: ")
                        if receiver in account.friendlist:
                            print("")
                            msg = input("Type your message: ")
                            account.send_message(msg, receiver)
                        else:
                            print("You can only message your friends.")
                    # Get out of manage account menu
                    elif inner_menu_choice == "9":
                        #choice = social_network_ui.mainMenu()
                        break
                    else:
                        print("Your input is invalid. Try Again!")          
            #restart menu
            choice = social_network_ui.mainMenu()


        elif choice == "3":
            print("Thank you for visiting. Goodbye!")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()




        
