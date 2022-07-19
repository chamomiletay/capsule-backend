from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('name', 'color', 'image', 'article_type', 'category', 'brand', 'quantity')