from django.contrib import admin
from .models import Article, Favorite

# Register your models here.
admin.site.register(Article)
admin.site.register(Favorite)