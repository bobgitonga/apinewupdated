

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"The book '{self.title}' has been borrowed.")
        else:
            print(f"The book '{self.title}' is already borrowed.")

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' was not borrowed.")


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
        else:
            print(f"Sorry, '{book.title}' is currently unavailable.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
        else:
            print(f"'{book.title}' is not borrowed by you.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"Books borrowed by {self.name}:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has no borrowed books.")


# Interactive code for borrowing and returning books
def interactive_library_system():
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

    member = LibraryMember("John Doe", "123")

    while True:
        print("\nLibrary Management System")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. List borrowed books")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nAvailable books:")
            print("1. 1984 by George Orwell")
            print("2. To Kill a Mockingbird by Harper Lee")
            print("3. The Great Gatsby by F. Scott Fitzgerald")
            book_choice = input("Enter the book number to borrow: ")

            if book_choice == '1':
                member.borrow_book(book1)
            elif book_choice == '2':
                member.borrow_book(book2)
            elif book_choice == '3':
                member.borrow_book(book3)
            else:
                print("Invalid choice.")

        elif choice == '2':
            print("\nBorrowed books:")
            member.list_borrowed_books()
            book_choice = input("Enter the book title to return: ")

            if book_choice == "1984":
                member.return_book(book1)
            elif book_choice == "To Kill a Mockingbird":
                member.return_book(book2)
            elif book_choice == "The Great Gatsby":
                member.return_book(book3)
            else:
                print("Invalid choice.")

        elif choice == '3':
            member.list_borrowed_books()

        elif choice == '4':
            print("Exiting system.")
            break

        else:
            print("Invalid choice.")

()
