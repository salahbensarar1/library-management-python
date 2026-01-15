from app.models.address import Address
from app.models.author import Author
from app.services.library import Library

address1 = Address("6000","Kecskemet","Gat Utca 41")
address2 = Address("6000","Kecskemet","Gat Utca 42")
author1 = Author("Salah","Ben Sarar")

libr = Library()
libr.add_member("waah1","WaahLN2",address1)
libr.add_member("waah2","WaahLN2",address2)
libr.add_book("Waahbook1",author1)
libr.add_book("WaahBook2",author1)

print(libr.borrow_book(1,1))
print(libr.return_book(1))
print("The books are: ",libr.books)

