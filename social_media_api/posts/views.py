from rest_framework import viewsets, permissions, generics, status
from .models import Notification, Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)

        # Check if the user has already liked the post
        if Like.objects.filter(post=post, user=request.user).exists():
            return Response({"detail": "You have already liked this post."}, status=400)

        # Create a Like entry
        like = Like.objects.create(post=post, user=request.user)

        # Create a notification for the post author
        notification = Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target_content_type=ContentType.objects.get_for_model(Post),
            target_object_id=post.id
        )

        return Response({"detail": "Post liked successfully"}, status=200)

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)

        # Check if the user has liked the post
        like = Like.objects.filter(post=post, user=request.user).first()
        if not like:
            return Response({"detail": "You haven't liked this post."}, status=400)

        # Delete the like
        like.delete()

        # Optionally, delete the notification
        Notification.objects.filter(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target_content_type=ContentType.objects.get_for_model(Post),
            target_object_id=post.id
        ).delete()

        return Response({"detail": "Post unliked successfully"}, status=200)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Save the comment with the author as the current user
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
