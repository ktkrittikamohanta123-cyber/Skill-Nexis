# Library Management System using OOP
# Features: add/remove books, issue/return books

class Library:
    def __init__(self):
        # Each book title is stored with its availability status.
        self.books = {}

    def add_book(self, title):
        title = title.strip()
        if not title:
            print("Book title cannot be empty.")
        elif title in self.books:
            print("This book is already in the library.")
        else:
            self.books[title] = True
            print(f'"{title}" added successfully.')

    def remove_book(self, title):
        if title not in self.books:
            print("Book not found.")
        elif self.books[title] is False:
            print("This book is currently issued. Return it before removing.")
        else:
            del self.books[title]
            print(f'"{title}" removed successfully.')

    def issue_book(self, title):
        if title not in self.books:
            print("Book not found.")
        elif self.books[title] is False:
            print("This book is already issued.")
        else:
            self.books[title] = False
            print(f'"{title}" issued successfully.')

    def return_book(self, title):
        if title not in self.books:
            print("Book not found in the library.")
        elif self.books[title] is True:
            print("This book was not issued.")
        else:
            self.books[title] = True
            print(f'"{title}" returned successfully.')

    def display_books(self):
        if not self.books:
            print("The library is empty.")
            return

        print("\n--- BOOK LIST ---")
        for title, available in self.books.items():
            status = "Available" if available else "Issued"
            print(f"{title} - {status}")


# Main program
library = Library()

while True:
    print("\n--- LIBRARY MENU ---")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        library.add_book(title)
    elif choice == "2":
        title = input("Enter book title to remove: ")
        library.remove_book(title)
    elif choice == "3":
        title = input("Enter book title to issue: ")
        library.issue_book(title)
    elif choice == "4":
        title = input("Enter book title to return: ")
        library.return_book(title)
    elif choice == "5":
        library.display_books()
    elif choice == "6":
        print("Exiting Library Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
