from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path("books/", list_books, name="list_books"),  # For the function-based view
    path(
        "library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"
    ),  # For the class-based view
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),  # Ensure you have this register view defined

]
