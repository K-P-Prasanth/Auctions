from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return f"{self.id} : {self.username}"
    


class create_listing(models.Model):
    title = models.CharField(max_length=20,null=False)
    description = models.CharField(max_length=100)
    st_bid = models.IntegerField()
    image = models.URLField()
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        null=True,
        related_name="auction_category",
    )
    owner = models.CharField(max_length=100)
    max_bidder = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} : {self.title} : {self.st_bid} "

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name}"
    

class watchlist(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_watching"
    )
    listings = models.ForeignKey(
        create_listing,
        on_delete=models.CASCADE,
        null=True,
        related_name="watched_item",
    )

    def __str__(self):
        return f"{self.listings.title} : {self.user.username}"
    