from app.models.address import Address
from app.models.author import Author
from app.models.book import Book
from app.models.member import Member
from app.services.library import Library

address1 = Address("6000","Kecskemet","Gat Utca 41")
author1 = Author("Salah","Ben Sarar")

libr = Library()
libr.add_member("waah","WaahLN",address1)
libr.add_book("Waahbook",author1)

print("The books are: ",libr.books)

