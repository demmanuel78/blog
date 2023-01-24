from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Category, Post, Comment

# Register your models here.

class AdminCategory(admin.ModelAdmin):
    list_display = ("name", )
    
class AdminPost(admin.ModelAdmin):
    list_display = ("title", "date", "pic", "category")    


class AdminComment(admin.ModelAdmin):
    list_display = ("user", "post", "date", "comment")




admin.site.register(User, UserAdmin)
admin.site.register(Category, AdminCategory)
admin.site.register(Post, AdminPost)
admin.site.register(Comment, AdminComment)


