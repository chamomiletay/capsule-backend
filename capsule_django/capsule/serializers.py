from rest_framework import serializers
from .models import Article, Favorite

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('id','user','name', 'color','article_type', 'category', 'brand', 'quantity')

class FavoriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'title')