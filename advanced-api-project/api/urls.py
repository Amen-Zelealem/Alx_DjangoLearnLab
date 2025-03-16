from django.urls import path
from .views import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    RetrieveView,
    DetailView,
)

urlpatterns = [
    path("books/", ListView.as_view(), name="book-list"),
    path("books/create/", CreateView.as_view(), name="book-create"),
    path("books/<int:pk>/", RetrieveView.as_view(), name="book-retrieve"),
    path("books/<int:pk>/update/", UpdateView.as_view(), name="book-update"),
    path("books/<int:pk>/delete/", DeleteView.as_view(), name="book-delete"),
    path("books/detail/<int:pk>/", DetailView.as_view(), name="book-detail"),
]
