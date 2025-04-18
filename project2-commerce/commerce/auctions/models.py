from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
class Category(models.Model):
    categoryName = models.CharField(max_length=50)
    def __str__(self):
        return self.categoryName
class Bid(models.Model):
    bid=models.IntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True, related_name="userBid")
    # def __str__(self):
    #     return self.bid
class Listing(models.Model):
    title=models.CharField(max_length=90)
    description=models.CharField(max_length=300)
    imageUrl=models.CharField(max_length=1000)
    price=models.ForeignKey(Bid,on_delete=models.CASCADE,blank=True,null=True,related_name="bidPrice")
    isActive=models.BooleanField(default=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="user")
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True,related_name="category")
#    watchlist for many to many relationship which is connected to listing.html
    watchlist=models.ManyToManyField(User,blank=True,null=True,related_name="listingWatchlist")
    def __str__(self):
        return self.title

class Comment(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="UserComment")
    listing=models.ForeignKey(Listing,on_delete=models.CASCADE,blank=True,null=True,related_name="listingComment")
    message=models.CharField(max_length=200)
    def ___str__(self):
        return f"{self.author} comment on {self.listing}"
