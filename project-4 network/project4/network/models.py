from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
class Post(models.Model):
    Content=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="author")
    Timestamp=models.DateTimeField(auto_now_add=True)
    # ImageUrl=models.ImageField(max_length=100)
    def __str__(self):
        return f"Post:{self.id} created by {self.user} on {self.Timestamp.strftime('%d %b %Y %H:%M:%S')}"
class Follow(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="following_user")
    user_follower=models.ForeignKey(User,on_delete=models.CASCADE,related_name="followed_user")
    def __str__(self):
        return f"{self.user}is Following{self.user_follower}"
class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_liked")
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="post_liked")
    def __str__(self):
        return f"${self.user} liked ${self.post}"