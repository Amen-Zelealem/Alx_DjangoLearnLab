from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment, Tag



# CustomUserCreationForm for creating a new user
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# PostForm for creating and editing blog posts with tags
class PostForm(forms.ModelForm):
    tags = forms.CharField(max_length=200, required=False, help_text="Enter tags separated by commas.")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        post = super().save(commit=False)
        tags = self.cleaned_data.get('tags')
        if tags:
            tag_list = [tag.strip() for tag in tags.split(',')]
            tags = [Tag.objects.get_or_create(name=tag)[0] for tag in tag_list]
            post.save()
            post.tags.set(tags)
        else:
            post.save()
        return post

# Added Comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'placeholder': 'Enter your comment here...'})