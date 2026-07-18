# Simple Library Management System using Class and Object

class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        self.books.append({"title": title, "author": author})
        print("Book added successfully!")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")

        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                print("Book removed successfully!")
                return

        print("Book not found.")

    def search_book(self):
        keyword = input("Enter title or author to search: ").lower()
        found = False

        for book in self.books:
            if keyword in book["title"].lower() or keyword in book["author"].lower():
                print(f"- {book['title']} by {book['author']}")
                found = True

        if not found:
            print("No matching books found.")

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("\nBooks in the library:")
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. {book['title']} by {book['author']}")


def show_menu():
    print("\nLibrary Management System")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Exit")


def main():
    library = Library()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.remove_book()
        elif choice == "3":
            library.search_book()
        elif choice == "4":
            library.display_books()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
