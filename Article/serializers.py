from rest_framework import serializers
from .models import Article, CategoryArticle, TagArticle
from drf_extra_fields.fields import Base64ImageField


class CategoryArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryArticle
        fields = (
            'id',
            'name',
            'created_at',
        )


class TagArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryArticle
        fields = (
            'id',
            'name',
            'created_at',
        )


class ArticleSerializer(serializers.ModelSerializer):
    categories_full = CategoryArticleSerializer(source='categories', many=True, read_only=True)
    tags_full = TagArticleSerializer(source='tags', many=True, read_only=True)
    image = Base64ImageField(required=False)

    class Meta:
        model = Article
        fields = (
            'id',
            'user',
            'title',
            'description',
            'image',
            'categories',
            'categories_full',
            'tags',
            'tags_full',
        )
