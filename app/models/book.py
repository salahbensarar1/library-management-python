class Book:
    def __init__(self, book_id, title, author, borrower_id=None):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.borrower_id = borrower_id

    def __str__(self):
        return f"Book(id={self.book_id}, title='{self.title}')"

    def __repr__(self):
        return self.__str__()