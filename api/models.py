from re import T
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy
from rest_framework.response import Response
from ckeditor.fields import RichTextField
from .article import Article


class User(AbstractUser):
    avartar = models.ImageField(upload_to="images/%Y/%m",
                                blank=True,
                                null=True,
                                default=None)

    def __str__(self) -> str:
        return str(self.username)

    def get_absolute_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.id})


# class Article(models.Model):
#     title = models.CharField(max_length=255)
#     # content = models.TextField()
#     content = RichTextField()
#     author = models.ForeignKey(User,
#                                null=True,
#                                blank=True,
#                                on_delete=models.SET_NULL)
#     date_published = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#     # tags = models.ManyToManyField(Tags, blank=True, related_name="Tag")
#     active = models.BooleanField(default=True)
#     tags = models.ManyToManyField('Tag', blank=True, related_name="article")

#     def __str__(self) -> str:
#         return str(self.title)


class Tag(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return str(self.user)


class Reply(models.Model):
    user = models.ForeignKey(User,
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    comment = models.ForeignKey('Comment',
                                null=True,
                                blank=True,
                                on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.user) + str(self.comment)


class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, unique=True)

    def __str__(self) -> str:
        return str(self.name)
