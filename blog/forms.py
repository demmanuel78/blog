from django import forms
from django.forms import fields
from .models import Comment, Post, User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm


class RForm(UserCreationForm):

    class Meta:
        model = User
        exclude = ("password", "last_login", "is_superuser", "is_staff", "is_active", "date_joined", "groups", "user_permissions")
        
class TForm(forms.ModelForm):
    
    class Meta:
        model = Post
        exclude =("post", "category", "user")
        
        
class CForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude=("post","user")
