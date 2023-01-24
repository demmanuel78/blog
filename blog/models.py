from django.db import models
from django.contrib.auth.models import AbstractUser
from blogProject import settings
# Create your models here.
#AbstractUser - AbstractBaseUser


class User(AbstractUser):
    gender = models.CharField(max_length=5)
    phone = models.CharField(max_length=14)
    email = models.EmailField(unique=True, blank=True, max_length=254, verbose_name='email address')
    
    class Meta:
        db_table = 'auth_user'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    category = models.ForeignKey(Category, verbose_name="Category",  on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="images/")
    date= models.DateTimeField(auto_now_add=True, editable=False)
    body = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")   
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments") 
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True, editable=False)   

    def __str__(self):
        return self.comment

        