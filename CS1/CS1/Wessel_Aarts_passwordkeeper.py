import random
import string
import csv

def list_entries(apps, usernames, passwords):
    if not apps:
        print("No entries yet.")
    for i in range(len(apps)):
        print("Website:  " + apps[i])
        print("Username: " + usernames[i])
        print("Password: " + passwords[i])
'''
DESCRIPTION
    This function prints out every single entry stored in the lists. Its useful if you forget what you saved.

Args:
    apps (list): A list of strings containing website names.
    usernames (list): A list of strings containing the usernames.
    passwords (list): A list of strings containing passwords.
Return/Print:
    Print (string): Displays the formatted data for each website.
Raises:
    N/A: No specific errors handled here.
'''

def access_entry(apps, usernames, passwords):
    search = input("What app are you looking for? ")
    
    if search in apps:
        i = apps.index(search)
        print("Website: " + apps[i])
        print("Username: " + usernames[i])
        print("Password: " + passwords[i])
    else:
        print("Not found.")
'''
DESCRIPTION
    Asks the user for a name and then it finds that name in the apps list. If it find it, it shows the info.

Args:
    apps (list): The list where app names are stored.
    usernames (list): The list where usernames are stored.
    passwords (list): The list where passwords are stored.
Return/Print:
    Print (string): Returns the found entry or a message saying not found.
Raises:
    ValueError: Occurs if the index search fails (though handled by 'if' check).
'''

def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    pas = []
    
   
    for i in range(length // 4):
        pas.append(random.choice(lowercase))
        pas.append(random.choice(uppercase))
        pas.append(random.choice(digits))
        pas.append(random.choice(punctuation))

    random.shuffle(pas)
    return ''.join(pas)
'''
DESCRIPTION
    Creates a random string for security. It mix letters, numbers and symbols together so its hard to guess.

Args:
    length (int): How long the password should be.
Return/Print:
    Return (string): The newly generated password string.
Raises:
    TypeError: If length is not an integer.
'''

def add_entry(apps, usernames, passwords):
    web = input("Website: ")
    user = input("Username: ")

    secure_password = input(
        "Would you like me to generate a secure password? (yes/no): "
    ).lower()

    if secure_password == "yes":
       
        pas = generate_password(12) 
        print("Generated password:", pas)
    else:
        pas = input("Enter your own password: ")

    apps.append(web)
    usernames.append(user)
    passwords.append(pas)
    print("Entry saved!")
'''
DESCRIPTION
    Allows user to add new website to the database. They can type there own password or get a random one.

Args:
    apps (list): The list for app names.
    usernames (list): The list for usernames.
    passwords (list): The list for passwords.
Return/Print:
    Print (string): Confirmation that the entry was saved.
Raises:
    N/A: Standard input used.
'''

def edit_entry(apps, usernames, passwords):
    search = input("Enter the website name you want to edit: ")
    
    if search in apps:
        i = apps.index(search)
        print(f"\nCurrent details for '{apps[i]}':")
        print("  Username: " + usernames[i])
        print("  Password: " + passwords[i])
    else:
        print("No entry found for that website.")
        return

    print("\nWhat would you like to change?")
    print("  1. Website name")
    print("  2. Username")
    print("  3. Password")
    print("  4. All fields")
    field = input("Choice: ")

    if field == "1" or field == "4":
        apps[i] = input("New website name: ")
    if field == "2" or field == "4":
        usernames[i] = input("New username: ")
    if field == "3" or field == "4":
        gen = input("Generate a secure password? (yes/no): ").lower()

        if gen == "yes":
            passwords[i] = generate_password(12)
            print("Generated password:", passwords[i])
        else:
            passwords[i] = input("New password: ")

    print("Entry updated!")
'''
DESCRIPTION
    This function lets you change stuff that is already saved in the arrays if you made a mistake.

Args:
    apps (list): List of apps.
    usernames (list): List of usernames.
    passwords (list): List of passwords.
Return/Print:
    Print (string): Success message once the update is finish.
Raises:
    N/A: Check for existence happens before editing.
'''


def export_entries(apps, usernames, passwords):
    data = zip(apps, usernames, passwords)

    with open('output.csv', 'w', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(['App', 'Username', 'Password'])
        writer.writerows(data)
    print('Data saved to CSV file')


def main():
    keeper_password = "orange"

    while True:
        attempt = input("Hello there, enter the password to access the keeper, hint its a six lettered fruit: ")

        if attempt == keeper_password:
            print("You are correct")
            break
        else:
            print("Incorrect password, its very obvious")

    # These are the three empty parallel arrays
    apps = []
    usernames = []
    passwords = []

    while True:
        print('''
(Press 'q' to quit)
1. See all entries
2. Access specific entry
3. Add entry
4. Edit entry
5. Access entries through Excel
        ''')

        choice = input("What would you like to do: ").lower()

        if choice == "q":
            print("Closing program.")
            break
        elif choice == "1":
            list_entries(apps, usernames, passwords)
        elif choice == "2":
            access_entry(apps, usernames, passwords)
        elif choice == "3":
            add_entry(apps, usernames, passwords)
        elif choice == "4":
            edit_entry(apps, usernames, passwords)
        elif choice == "5":
            export_entries(apps, usernames, passwords)
        else:
            print("Invalid choice, please try again.")
'''
DESCRIPTION
    The main part of the script. It handles the login security and the main menu loop for the user.

Args:
    None: Takes no arguments.
Return/Print:
    Print (string): Various menu options and prompts.
Raises:
    KeyboardInterrupt: If user force quits the terminal.
'''

if __name__ == "__main__":
    main()


    