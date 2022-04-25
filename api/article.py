from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.response import Response
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=255)
    # content = models.TextField()
    content = RichTextField()
    author = models.ForeignKey('User',
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name="article")

    def __str__(self) -> str:
        return str(self.title)

    def get_absolute_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.id})