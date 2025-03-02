from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django.http import Http404
from .models import Book

# View to list all books
@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'bookshelf/book_list.html', {'books': books})

# View to create a new book
@permission_required('bookshelf.can_create_book', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        isbn = request.POST.get('isbn')

        # Create the book
        Book.objects.create(
            title=title,
            author=author,
            published_date=published_date,
            isbn=isbn
        )
        return redirect('book_list')  # Redirect to the book list view

    return render(request, 'bookshelf/create_book.html')

# View to edit a book
@permission_required('bookshelf.can_edit_book', raise_exception=True)
def edit_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("Book not found")

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.published_date = request.POST.get('published_date')
        book.isbn = request.POST.get('isbn')
        book.save()
        return redirect('book_list')  # Redirect to the book list view

    return render(request, 'bookshelf/edit_book.html', {'book': book})

# View to delete a book
@permission_required('bookshelf.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("Book not found")

    book.delete()
    return redirect('book_list')  # Redirect to the book list view
