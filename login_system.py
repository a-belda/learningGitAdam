# Users will be stored as: username;password;email;phone\n

def register():
    print("Register a Gemu account")
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")

    with open("users.txt", "a") as file:
        file.write(f"{username};{password};{email};{phone}\n")

    print("Successfully registered! You can now login.\n")
    return login()

def login():
    print("*" * 30)
    print("Welcome to the Gemucube Technology")
    print("*" * 30)
    print("1. Login")
    print("2. Register")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if(username == "" or password == ""):
            print("Please provide both username and password.")
            return login()

        with open("users.txt", "r") as file:
            for line in file:
                temp_username, temp_password, _, _ = line.replace("\n", "").split(";")
                
                if(username == temp_username and password == temp_password):
                    print(f"Hello, {username}! Welcome to the Gemucube Technology!")
                    return True
            
        print("Incorrect username or password. Please try again.")
        return login()
        
    elif choice == "2":
        return register()

    else:
        print("Invalid choice. Please enter 1 or 2.")
        return login()

if __name__ == '__main__':
    login()