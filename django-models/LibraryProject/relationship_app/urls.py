# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView
from .views import login_view, logout_view, register


urlpatterns = [
    path("books/", list_books, name="list_books"),  # For the function-based view
    path(
        "library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"
    ),  # For the class-based view
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register, name="register"),
]
