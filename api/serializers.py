from rest_framework.serializers import ModelSerializer, SerializerMethodField, HyperlinkedModelSerializer
from .models import User, Article, Comment, Tag, Reply, Category
from rest_framework import serializers


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)


class TagSerializer(ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name']
        # fields = "__all__"


class ArticleSerializer(ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = "__all__"


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class ReplySerializer(ModelSerializer):

    class Meta:
        model = Reply
        fields = "__all__"


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
