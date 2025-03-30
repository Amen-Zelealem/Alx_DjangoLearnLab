from rest_framework import viewsets, permissions, generics, status
from .models import Notification, Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework import filters
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound


User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by("-created_at")


class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Get the post and the user
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound("Post not found")

        user = request.user

        # Prevent users from liking their own posts
        if post.author == user:
            return Response(
                {"detail": "You cannot like your own post."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # If the user has already liked the post, return a response
        if Like.objects.filter(post=post, user=user).exists():
            return Response(
                {"detail": "You already liked this post."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Create the like
        Like.objects.create(post=post, user=user)

        # Create a notification for the post author
        Notification.objects.create(
            recipient=post.author, actor=user, verb="liked your post", target=post
        )

        return Response(
            {"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED
        )


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Get the post and the user
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound("Post not found")

        user = request.user

        # Ensure the user has liked the post
        try:
            like = Like.objects.get(post=post, user=user)
        except Like.DoesNotExist:
            return Response(
                {"detail": "You haven't liked this post."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Delete the like
        like.delete()

        return Response(
            {"detail": "Post unliked successfully."}, status=status.HTTP_204_NO_CONTENT
        )
