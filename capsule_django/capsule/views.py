#---- i m p o r t s ! ----
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import generics, permissions, status 
from .models import Article, Favorite
from .serializers import ArticleSerializer, FavoriteSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
import random


#---- v i e w s ! ----
def working(request):
    return HttpResponse('Hello, I am working!')


#---- test auth routes ----
def test_login(request):
    return JsonResponse({'loggedIn':True, 'username': 'test_user'})

def test_signup(request):
    return JsonResponse({'loggedIn': True, 'username': 'test_user'})    


#--- display wardrobe items ---
def show_articles(request):
    articles = Article.objects.all().values()
    articles_list = list(articles)
    return JsonResponse(articles_list, safe=False)

#--- display API view for wardrobe items (CR)---
# class CreateArticle(APIView):
#     parser_classes = [MultiPartParser, FormParser]

#     def post(self, request, format=None):
#         print(request.data)
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

#     # def add(self, request, *args, **kwargs):
#     #     request.data['user_string'] = request.user.username
#     #     return super().add(request, *args, **kwargs)

class ViewArticle(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

#     # --- authentication check ---
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
#--- (RUD) permissions ---
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

#--- (RUD) permissions ---
class ArticleDetailProtected(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    permission_classes = [permissions.IsAuthenticated]

#--- Protected route - wardrobe ---
class ArticleListProtected(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    permission_classes = [permissions.IsAuthenticated]

#--- Protected route - randomizer ---
class NewOutfitProtected(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    permission_classes = [permissions.IsAuthenticated]

#--- Favorites data (unprotected) ---
class FavoritesView(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()

#--- (RUD) permissions ---
class FavoritesDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()
