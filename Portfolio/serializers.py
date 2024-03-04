from rest_framework import serializers
from .models import Portfolio
from Article.serializers import CategoryArticleSerializer, TagArticleSerializer
from drf_extra_fields.fields import Base64ImageField


class PortfoliosSerializer(serializers.ModelSerializer):
    categories_full = CategoryArticleSerializer(source='categories', many=True, read_only=True)
    tags_full = TagArticleSerializer(source='tags', many=True, read_only=True)
    image = Base64ImageField(required=False)

    class Meta:
        model = Portfolio
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
