
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_post",views.new_post, name="new_post"),
    path("profile_post/<int:user_id>", views.profile_post,name="profile_post"),
    path("follow",views.follow, name="follow"),
    path("unfollow",views.unfollow, name="unfollow"),
    path("following",views.following, name="following"),
    path("edit/<int:post_id>",views.edit,name="edit"),
    path("remove/<int:post_id>",views.remove,name="remove"),
    path("add/<int:post_id>",views.add,name="add"),
]
    

