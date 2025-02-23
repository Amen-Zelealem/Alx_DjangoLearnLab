from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = Author.objects.get(name="Author Name")
books_by_author = Book.objects.filter(author=author_name)
for book in books_by_author:
    print(book.title)

# List all books in a library
library_name = Library.objects.get(name="Library Name")
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
for book in books_in_library:
    print(book.title)

# Retrieve the librarian for a library
library = Library.objects.get(name="Library Name")
librarian = Librarian.objects.get(library=library)
print(librarian.name)
