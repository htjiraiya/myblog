from statistics import mode
from django.shortcuts import render
from api.models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q


class ArticleList(ListView):
    model = Article
    template_name = 'blogbootstrap/article_list.html'
    paginate_by = 4
    # object_list = Article.objects.all()[0]


class ArticleDetail(DetailView):
    model = Article
    template_name = 'blogbootstrap/article_detail.html'


class Search(ListView):
    model = Article
    template_name = 'blogbootstrap/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Article.objects.filter(title__icontains=query)
        return object_list
