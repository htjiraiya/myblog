from turtle import mode
from django.contrib import admin
from .models import (User, Article, Comment, Tag, Reply, Category)
from ckeditor.widgets import CKEditorWidget
from django import forms
# from api.models import Article
from api.article import Article


class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = "__all__"


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm


admin.site.register(User)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Reply)
admin.site.register(Category)
