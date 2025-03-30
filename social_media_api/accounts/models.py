from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    # Update related_name to avoid clashes
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following_users', blank=True)
    following = models.ManyToManyField("self", symmetrical=False, related_name="followers_users", blank=True)

    # Add related_name to avoid clashes with the default User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser'
    )
