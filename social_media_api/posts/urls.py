from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LikePostView, PostViewSet, CommentViewSet, PostFeedView, UnlikePostView

router = DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("feed/", PostFeedView.as_view(), name="post_feed"),
    path('<int:pk>/like/', LikePostView.as_view(), name='like_post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike_post'),
]
