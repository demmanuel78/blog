from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", views.index, name="home"),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name = "blog/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("category/createpost/<id>", views.createpost, name="createpost"),
    path("category/<id>", views.postcategory, name="category"),
    path("post_details/<id>", views.post_details, name="post_details"),
    path("recent/", views.recentpost, name="recentpost"),
    path("userpost/<id>", views.userpost, name="userpost"),
    path("search/", views.search, name="search"),
    path("update/user/<id>", views.updateprofile, name="updateprofile")
]


