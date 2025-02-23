from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from relationship_app.models import Library

# Create your views here.
from relationship_app.models import Book


def list_books(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
