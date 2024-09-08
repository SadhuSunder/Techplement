import re

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

def validate_phone(phone):
    # Validate phone number
    pattern = r"^\d{10}$"
    return re.match(pattern, phone) is not None

def validate_email(email):
    # Validate email 
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print(f"Contact with name {name} already exists.")
        else:
            if not validate_phone(phone):
                print("Invalid phone number. It should be 10 digits.")
                return
            if not validate_email(email):
                print("Invalid email address.")
                return
            self.contacts[name] = Contact(name, phone, email)
            print(f"Contact {name} added successfully.")

    def search_contact(self, name):
        contact = self.contacts.get(name)
        if contact:
            print(contact)
        else:
            print(f"No contact found with name {name}.")

    def update_contact(self, name, phone=None, email=None):
        contact = self.contacts.get(name)
        if contact:
            if phone:
                if not validate_phone(phone):
                    print("Invalid phone number. It should be 10 digits.")
                    return
                contact.phone = phone
            if email:
                if not validate_email(email):
                    print("Invalid email address.")
                    return
                contact.email = email
            print(f"Contact {name} updated successfully.")
        else:
            print(f"No contact found with name {name}.")

    def display_all_contacts(self):
        if self.contacts:
            for contact in self.contacts.values():
                print(contact)
        else:
            print("No contacts available.")

    def save_contacts(self, filename="contacts.txt"):
        with open(filename, "w") as file:
            for contact in self.contacts.values():
                file.write(f"{contact.name},{contact.phone},{contact.email}\n")
        print(f"Contacts saved to {filename}.")

    def load_contacts(self, filename="contacts.txt"):
        try:
            with open(filename, "r") as file:
                for line in file:
                    name, phone, email = line.strip().split(",")
                    self.contacts[name] = Contact(name, phone, email)
            print(f"Contacts loaded from {filename}.")
        except FileNotFoundError:
            print(f"No file named {filename} found.")

def main():
    manager = ContactManager()
    manager.load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Display All Contacts")
        print("5. Save Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            manager.add_contact(name, phone, email)

        elif choice == "2":
            name = input("Enter name to search: ")
            manager.search_contact(name)

        elif choice == "3":
            name = input("Enter name to update: ")
            phone = input("Enter new phone (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            manager.update_contact(name, phone if phone else None, email if email else None)

        elif choice == "4":
            manager.display_all_contacts()

        elif choice == "5":
            manager.save_contacts()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
