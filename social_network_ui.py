# You can implement user interface functions here.

# You can implement user interface functions here.

def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")


def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4 Block a friend")
    print("5. View all blocked friends")
    print("6. Unblock Friend")
    print("7. Send a message")
    print("8. View all my messages")
    print("9. <- Go back ")
    return input("Please Choose a number: ")

# Interface for editing the account
def editDetail():
    print("")
    print("1. Edit my Username")
    print("2. Edit my Password")
    print("3.<- Go back  ")
    return input("Please Choose a number: ")
