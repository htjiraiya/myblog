from re import S
from rest_framework import permissions
from django.http import HttpResponse
from rest_framework import viewsets
from api.serializers import (UserSerializer, ArticleSerializer,
                             CommentSerializer, ReplySerializer, TagSerializer,
                             CategorySerializer)

from api.models import User, Category, Comment, Article, Tag, Reply
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response

from api.serializers import *
# from viewstemplate import *

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(methods=['get'], detail=True)
    def show(self, request, pk):
        # if request.user.has_perm("api.retrieve"):
        if request.user.username != "admin":

            user = User.objects.get(id=pk)
            userSerializer = UserSerializer(user).data
            return Response(userSerializer, status=status.HTTP_200_OK)
        return Response("deo admin a ", status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response("no", status=status.HTTP_404_NOT_FOUND)

    # def retrieve(self, request, pk):
    #     if request.user.has_perm("api.retrieve"):
    #         user = User.objects.get(id=pk)
    #         userSerializer = UserSerializer(user).data
    #         return Response(userSerializer, status=status.HTTP_200_OK)
    #     return Response("deo", status=status.HTTP_400_BAD_REQUEST)


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.filter(active=True)
    # permission_classes = [permissions.IsAuthenticated]

    @action(methods=["post"], detail=True)
    def hide_action(self, request, pk):
        try:
            article = Article.objects.get(id=pk)
            article.active = False
            article.save()
            return Response(
                ArticleSerializer(article).data,
                status=status.HTTP_200_OK,
            )
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_context(self):
        return {'request': self.request}


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(active=True)
    permission_classes = [permissions.IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        if self.get_object().user == request.user:
            super().partial_update(request, *args, **kwargs)
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_403_FORBIDDEN)


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class ReplyViewSet(viewsets.ModelViewSet):
    serializer_class = ReplySerializer
    queryset = Reply.objects.filter(active=True)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_permissions(self):
        if self.action in ['list']:
            return [permissions.AllowAny()]

        return [permissions.IsAuthenticated()]

    # def partial_update(self, request, *args, **kwargs):
    #     if self.get_object().user == request.user:
    #         super().partial_update(request, *args, **kwargs)
    #         return Response(status=status.HTTP_202_ACCEPTED)
    #     return Response(status=status.HTTP_403_FORBIDDEN)