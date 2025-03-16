from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# ✅ ListView - Allows anyone to read, but only authenticated users can create
class ListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Setup filtering, searching, and ordering
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    
    # Define fields to filter by
    filterset_fields = ['title', 'author', 'publication_year']
    
    # Define fields for searching
    search_fields = ['title', 'author']
    
    # Define fields that can be used for ordering
    ordering_fields = ['title', 'publication_year']
    
    # Default ordering by title
    ordering = ['title']




# ✅ CreateView - Only authenticated users can create
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ✅ UpdateView - Only authenticated users can update
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ✅ DeleteView - Only authenticated users can delete
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ✅ RetrieveView - Anyone can retrieve book details
class RetrieveView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ✅ DetailView - Read access for everyone, but only authenticated users can update/delete
class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
