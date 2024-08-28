from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    birthDate = models.DateField(null=True)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author = models.OneToOneField(Author, on_delete=models.PROTECT)     # one to one
    author = models.ForeignKey(Author, on_delete=models.PROTECT)        # one to many
    tag = models.ManyToManyField(Tag)   # we can use (Tag, related_name='Article') to set a default name