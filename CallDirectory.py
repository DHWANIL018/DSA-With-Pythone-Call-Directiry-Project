class Node:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.next = None


class TelephoneDirectory:
    def __init__(self):
        self.head = None

    def add_contact(self, name, phone):
        new_contact = Node(name, phone)
        new_contact.next = self.head
        self.head = new_contact
        print(f'Contact {name} added successfully.')

    def search_contact(self, name):
        current = self.head
        while current:
            if current.name.lower() == name.lower():
                return current.phone
            current = current.next
        return None

    def modify_contact(self, name, new_phone):
        current = self.head
        while current:
            if current.name.lower() == name.lower():
                current.phone = new_phone
                print(f'Contact {name} modified successfully.')
                return
            current = current.next
        print('Contact not found.')

    def list_contacts(self):
        current = self.head
        if current is None:
            print("No contacts found.")
            return
        while current:
            print(f'Name: {current.name}, Phone: {current.phone}')
            current = current.next

    def delete_contact(self, name):
        current = self.head
        previous = None
        while current:
            if current.name.lower() == name.lower():
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                print(f'Contact {name} deleted successfully.')
                return
            previous = current
            current = current.next
        print('Contact not found.')


# Main Program
def main():
    directory = TelephoneDirectory()
    while True:
        print("\nTelephone Directory System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Modify Contact")
        print("4. List Contacts")
        print("5. Delete Contact")
        print("6. Exit")
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            directory.add_contact(name, phone)
        elif choice == 2:
            name = input("Enter name to search: ")
            phone = directory.search_contact(name)
            if phone:
                print(f'Phone number for {name}: {phone}')
            else:
                print('Contact not found.')
        elif choice == 3:
            name = input("Enter name to modify: ")
            new_phone = input("Enter new phone number: ")
            directory.modify_contact(name, new_phone)
        elif choice == 4:
            directory.list_contacts()
        elif choice == 5:
            name = input("Enter name to delete: ")
            directory.delete_contact(name)
        elif choice == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
