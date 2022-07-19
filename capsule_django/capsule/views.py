#---- i m p o r t s ! ----
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import generics, permissions
from .models import Article
from .serializers import ArticleSerializer


#---- v i e w s ! ----
def working(request):
    return HttpResponse('Hello, I am working!')

#--- display wardrobe items ---
def show_articles(request):
    articles = Article.objects.all().values()
    articles_list = list(articles)
    return JsonResponse(articles_list, safe=False)