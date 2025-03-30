from django.urls import path
from . import views
from .views import CustomLoginView, CustomLogoutView, register, profile
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    # Authentication URLs
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),

    # Blog Post URLs
    path('', PostListView.as_view(), name='home'),  
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'), 
    path('post/new/', PostCreateView.as_view(), name='post_create'),  
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'), 
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  
]
