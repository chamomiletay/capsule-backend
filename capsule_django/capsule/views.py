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

#--- display API view for wardrobe items (CR)---
class ArticleList(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    #--- authentication check ---
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def add(self, request, *args, **kwargs):
    #     request.data['user_string'] = request.user.username
    #     return super().add(request, *args, **kwargs)

#--- (RUD) permissions ---
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

#--- Protected route - wardrobe ---
class ArticleListProtected(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    permission_classes = [permissions.IsAuthenticated]