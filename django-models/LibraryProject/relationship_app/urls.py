from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book

from . import views


urlpatterns = [
    path("books/", list_books, name="list_books"),  # For the function-based view
    path(
        "library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"
    ),  # For the class-based view
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path(
        "register/", views.register, name="register"
    ),  # Ensure you have this register view defined
    path("admin-view/", admin_view, name="admin_view"),
    path("librarian-view/", librarian_view, name="librarian_view"),
    path("member-view/", member_view, name="member_view"),
    # Book
    path("books/add/", add_book, name="add_book/"),
    path("books/<int:pk>/edit/", edit_book, name="edit_book/"),
    path("books/<int:pk>/delete/", delete_book, name="delete_book/"),
]
