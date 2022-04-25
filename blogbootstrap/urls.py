from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'blogbootstrap'

urlpatterns = [
    path('<pk>', ArticleDetail.as_view(), name='detail'),
    path('', ArticleList.as_view(), name='home'),
    path('search/', Search.as_view(), name='search'),
]
