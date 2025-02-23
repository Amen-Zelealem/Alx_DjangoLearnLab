from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from relationship_app.models import Library
from .models import Library
from django.views.generic.detail import DetailView

# Create your views here.
from relationship_app.models import Book


def list_books(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log the user in after successful registration
            login(request, user)
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

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
