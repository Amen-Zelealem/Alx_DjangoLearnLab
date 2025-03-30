from django.urls import path
from . import views
from .views import CustomLoginView, CustomLogoutView, register, profile
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    # Authentication
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),

    # Blog Post URLs
    path('', PostListView.as_view(), name='home'),  # Home page, list of all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Post detail view
    path('post/new/', PostCreateView.as_view(), name='post_create'),  # Create new post
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),  # Edit post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # Delete post
]
