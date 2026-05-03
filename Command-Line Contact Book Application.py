# Command-Line Contact Book Application
# Contacts are stored in a text file

FILE_NAME = "contacts.txt"

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    file = open(FILE_NAME, "a")
    file.write(f"Name: {name}, Phone: {phone}, Email: {email}\n")
    file.close()

    print("Contact added successfully!\n")


def view_contacts():
    try:
        file = open(FILE_NAME, "r")
        contacts = file.read()
        file.close()

        if contacts == "":
            print("No contacts found.\n")
        else:
            print("\n--- Contact List ---")
            print(contacts)
    except FileNotFoundError:
        print("No contacts file found.\n")


def search_contact():
    search_name = input("Enter name to search: ")
    found = False

    try:
        file = open(FILE_NAME, "r")
        for line in file:
            if search_name.lower() in line.lower():
                print("\nContact Found:")
                print(line)
                found = True
        file.close()

        if not found:
            print("Contact not found.\n")

    except FileNotFoundError:
        print("No contacts file found.\n")


# Main program
while True:
    print("===== Contact Book Menu =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
