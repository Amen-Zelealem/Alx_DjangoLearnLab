from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from relationship_app.models import Library
from .models import Library

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from django.views.generic.detail import DetailView


from django.contrib.auth.decorators import permission_required
from relationship_app.forms import BookForm

# Create your views here.
from relationship_app.models import Book


# View to add a book
@permission_required("relationship_app.can_add_book", login_url="/login/")
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_books")  # Redirect to the list of books
    else:
        form = BookForm()
    return render(request, "relationship_app/add_book.html", {"form": form})


# View to edit a book
@permission_required("relationship_app.can_change_book", login_url="/login/")
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm(instance=book)
    return render(
        request, "relationship_app/edit_book.html", {"form": form, "book": book}
    )


# View to delete a book
@permission_required("relationship_app.can_delete_book", login_url="/login/")
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "relationship_app/delete_book.html", {"book": book})


# Helper functions to check user roles
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == "Admin"


def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == "Librarian"


def is_member(user):
    return user.is_authenticated and user.userprofile.role == "Member"


# Views for role-based access
@user_passes_test(is_admin, login_url="/login/")
def admin_view(request):
    return render(
        request, "relationship_app/admin_view.html", {"message": "Welcome, Admin!"}
    )


@user_passes_test(is_librarian, login_url="/login/")
def librarian_view(request):
    return render(
        request,
        "relationship_app/librarian_view.html",
        {"message": "Welcome, Librarian!"},
    )


@user_passes_test(is_member, login_url="/login/")
def member_view(request):
    return render(
        request, "relationship_app/member_view.html", {"message": "Welcome, Member!"}
    )


def list_books(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# Registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log the user in after successful registration
            login(request, user)
            return redirect("login")  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Redirect to home page after login
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


# Logout view
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")
