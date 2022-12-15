from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.CharField(max_length=50)
    title = models.CharField(max_length=75)
    description = models.TextField(max_length=300)
    category = models.CharField(max_length=15)
    price = models.PositiveSmallIntegerField(null=False, default="1")
    url = models.CharField(max_length=150, default=None, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner

    # Listing from newest to oldest
    class Meta:
        ordering = ['-time']


class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=50)
    title = models.CharField(max_length=70)
    listingid = models.PositiveBigIntegerField(null=False)
    bid = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.user


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=300)
    listingid = models.PositiveBigIntegerField(null=False)

    def __str__(self):
        return self.user

    # Comments from newest to oldest
    class Meta:
        ordering = ['-time']


class Watchlist(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=50)
    listingid = models.PositiveBigIntegerField(null=False)

    def __str__(self):
        return self.user


class Closedbid(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.CharField(max_length=50)
    winner = models.CharField(max_length=50)
    listingid = models.PositiveBigIntegerField(null=False)
    winprice = models.PositiveSmallIntegerField(null=False)

    def __str__(self):
        return self.owner


class Alllisting(models.Model):
    id = models.AutoField(primary_key=True)
    listingid = models.PositiveBigIntegerField(null=False)
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=300)
    url = models.CharField(max_length=150, default=None, blank=True, null=True)
