from library_management_system import Book, Member, Library

# test the Book class
def test_book_display_info():
    book = Book(1, "1984", "George Orwell", 2)
    info = book.display_info()
    assert "1984" in info
    assert "George Orwell" in info

# test the Member class
def test_member_display_info():
    member = Member(1, "Patricia")
    info = member.display_info()
    assert "Patricia" in info

# test adding a book
def test_add_book():
    library = Library()
    book = Book(1, "1984", "George Orwell", 2)
    library.add_book(book)
    assert 1 in library.books

# test removing a book
def test_remove_book():
    library = Library()
    book = Book(1, "1984", "George Orwell", 2)
    library.add_book(book)
    library.remove_book(1)
    assert 1 not in library.books

# test adding a member
def test_add_member():
    library = Library()
    member = Member(1, "Patricia")
    library.add_member(member)
    assert 1 in library.members

# test removing a member
def test_remove_member():
    library = Library()
    member = Member(1, "Patricia")
    library.add_member(member)
    library.remove_member(1)
    assert 1 not in library.members

# test borrowing a book
def test_issue_book():
    library = Library()
    book = Book(1, "1984", "George Orwell", 2)
    member = Member(1, "Patricia")
    library.add_book(book)
    library.add_member(member)
    library.issue_book(1, 1)
    assert book in member.borrowed_books
    assert book.copies == 1  # copies should go down by 1

# test returning a book
def test_return_book():
    library = Library()
    book = Book(1, "1984", "George Orwell", 2)
    member = Member(1, "Patricia")
    library.add_book(book)
    library.add_member(member)
    library.issue_book(1, 1)
    library.return_book(1, 1)
    assert book not in member.borrowed_books
    assert book.copies == 2  # copies should be back to 2

# test you can't borrow a book with 0 copies
def test_issue_book_no_copies():
    library = Library()
    book = Book(1, "1984", "George Orwell", 0)  # 0 copies from the start
    member = Member(1, "Patricia")
    library.add_book(book)
    library.add_member(member)
    library.issue_book(1, 1)
    assert book not in member.borrowed_books  # should not have been borrowed

# test updating a book
def test_update_book():
    library = Library()
    book = Book(1, "1984", "George Orwell", 2)
    library.add_book(book)
    library.update_book(1, title="Animal Farm")
    assert library.books[1].title == "Animal Farm"