from django.contrib.sessions.models import Session
from django.db import models
from book_store import settings
from checkout.models import Transaction

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField(null=True)
    description = models.TextField(null=True)
    pdf_file = models.FileField(null=True)
    image = models.ImageField()
    price = models.FloatField()
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    @property
    def pdf_file_url(self):
        return settings.SITE_URL + self.pdf_file.url

    def __str__(self):
        return self.name


class Order(models.Model):
    transaction = models.OneToOneField(Transaction, on_delete=models.PROTECT, null=True)
    # customer = models.JSONField(default=dict)
    # total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # @property
    # def customer_name(self):
    #     return self.customer['first_name'] + ' ' + self.customer['last_name']

    def __str__(self):
        return self.id


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)



class Cart(models.Model):
    item = models.JSONField(default=dict)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)


class Slider(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField(max_length=500)
    image = models.ImageField(null=True)
    order = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title