class Member:
    def __init__(self, member_id,first_name, last_name, address):
        self.member_id = member_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.borrowed_books_count = 0