from app.models.member import Member
from app.models.book import Book
class Library:
    def __init__(self):
        self.members = []
        self.books = []

    def next_member_id(self):
       if not self.members:
           return 1
       return  max(member.member_id for member in self.members)+1
    def next_book_id(self):
       if not self.books:
           return 1
       return max(book.book_id for book in self.books)+1
    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book

    def add_member(self, first_name, last_name, address):
        member_id = self.next_member_id()
        new_member = Member(member_id, first_name, last_name, address)
        self.members.append(new_member)
        return new_member
    def add_book(self,title, author):
        book_id = self.next_book_id()
        new_book = Book(book_id, title, author)
        self.books.append(new_book)
        return new_book
