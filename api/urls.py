from django.urls import path, include, re_path
from api.views import *
from rest_framework.routers import DefaultRouter

app_name = "api"

router = DefaultRouter()
router.register('user', UserViewSet)
router.register('category', CategoryViewSet)
router.register('tag', TagViewSet)
router.register('comment', CommentViewSet)
router.register('article', ArticleViewSet)
router.register('reply', ReplyViewSet)

urlpatterns = [
    path('', include((router.urls, app_name))),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls'))
]
