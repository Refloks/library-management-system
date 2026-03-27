# base classes so I can use them later on
class LibraryItem:
    # parent class for books
    def __init__(self, item_id, title):
        self.item_id = item_id
        self.title = title

    def display_info(self):
        # this gets overridden by child classes
        return f"Item ID: {self.item_id}, Title: {self.title}"


class Person:
    # parent class for members
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

    def display_info(self):
        # this gets overridden by child classes
        return f"ID: {self.person_id}, Name: {self.name}"


# book inheritance from LibraryItem
class Book(LibraryItem):
    def __init__(self, book_id, title, author, copies):
        super().__init__(book_id, title)  # call parent constructor
        self.author = author
        self.copies = copies

    def display_info(self):
        return (f"Book ID: {self.item_id} | Title: {self.title} | "
                f"Author: {self.author} | Copies available: {self.copies}")


# member inheritance from Person
class Member(Person):
    def __init__(self, member_id, name):
        super().__init__(member_id, name)  # call parent constructor
        self.borrowed_books = []  # empty list to store borrowed books

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        else:
            print("You have not borrowed this book.")

    def display_info(self):
        # overrides the parent method
        borrowed = (", ".join(b.title for b in self.borrowed_books)
                    if self.borrowed_books else "None")
        return (f"Member ID: {self.person_id} | Name: {self.name} | "
                f"Borrowed books: {borrowed}")


# class that ties everything together
class Library:
    def __init__(self):
        # changed to dicts so I can look up by ID
        self.books = {}
        self.members = {}

    def add_book(self, book):
        if book.item_id in self.books:
            print(f"Error: Book ID {book.item_id} already exists.")
        else:
            self.books[book.item_id] = book
            print(f"Book '{book.title}' added.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed = self.books.pop(book_id)
            print(f"Book '{removed.title}' removed.")
        else:
            print(f"Error: No book with ID {book_id} found.")

    def update_book(self, book_id, title=None, author=None, copies=None):
        if book_id not in self.books:
            print(f"Error: No book with ID {book_id} found.")
            return
        book = self.books[book_id]
        # only update fields that were passed in
        if title:
            book.title = title
        if author:
            book.author = author
        if copies is not None:
            book.copies = copies
        print(f"Book ID {book_id} updated.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("\n--- Books ---")
        for book in self.books.values():
            print(book.display_info())  # polymorphism - calls Book's display_info
        print("-" * 40)

    def add_member(self, member):
        if member.person_id in self.members:
            print(f"Error: Member ID {member.person_id} already exists.")
        else:
            self.members[member.person_id] = member
            print(f"Member '{member.name}' added.")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed = self.members.pop(member_id)
            print(f"Member '{removed.name}' removed.")
        else:
            print(f"Error: No member with ID {member_id} found.")

    def update_member(self, member_id, name=None):
        if member_id not in self.members:
            print(f"Error: No member with ID {member_id} found.")
            return
        if name:
            self.members[member_id].name = name
        print(f"Member ID {member_id} updated.")

    def display_members(self):
        if not self.members:
            print("No members in the library.")
            return
        print("\n--- Members ---")
        for member in self.members.values():
            print(member.display_info())  # polymorphism - calls Member's display_info
        print("-" * 40)

    def issue_book(self, book_id, member_id):
        # check both exist before doing anything
        if book_id not in self.books:
            print(f"Error: No book with ID {book_id} found.")
            return
        if member_id not in self.members:
            print(f"Error: No member with ID {member_id} found.")
            return
        book = self.books[book_id]
        member = self.members[member_id]
        if book.copies <= 0:
            print(f"Error: No copies of '{book.title}' available.")
        else:
            book.copies -= 1
            member.borrow_book(book)
            print(f"'{book.title}' issued to {member.name}.")

    def return_book(self, book_id, member_id):
        if book_id not in self.books:
            print(f"Error: No book with ID {book_id} found.")
            return
        if member_id not in self.members:
            print(f"Error: No member with ID {member_id} found.")
            return
        book = self.books[book_id]
        member = self.members[member_id]
        if book not in member.borrowed_books:
            print(f"Error: {member.name} has not borrowed '{book.title}'.")
        else:
            member.return_book(book)
            book.copies += 1  # add the copy back
            print(f"'{book.title}' returned by {member.name}.")


if __name__ == "__main__":
    library = Library()

    # add some books to test with
    book1 = Book(1, "American Psycho", "Bret Easton Ellis", 3)
    book2 = Book(2, "1984", "George Orwell", 2)
    library.add_book(book1)
    library.add_book(book2)

    # add some members
    member1 = Member(1, "Patricia")
    member2 = Member(2, "Ole")
    library.add_member(member1)
    library.add_member(member2)

    library.display_books()
    library.display_members()

    # try borrowing and returning
    library.issue_book(1, 1)   # Patricia borrows book 1
    library.issue_book(2, 2)   # Ole borrows book 2
    library.return_book(1, 1)  # Atricia returns book 1
    library.return_book(2, 2)  # Ole returns book 2

    library.display_books()
    library.display_members()