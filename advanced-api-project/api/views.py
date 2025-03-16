from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List all books (GET) and Create a new book (POST)
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Restrict Create to authenticated users
    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

# Retrieve, Update, or Delete a book by ID
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Restrict Update & Delete to authenticated users
    def get_permissions(self):
        if self.request.method in ["PUT", "DELETE"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
