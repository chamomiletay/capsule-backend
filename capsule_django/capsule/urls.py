#---- i m p o r t s ! ----
from typing import ItemsView
from django.urls import path
from . import views

#-- brain dump --
    #---- links needed: ----
    # - display list of wardrobe items
    # - display saved outfits
    # - user signin
    # - user registration
##-- end brain dump --

#---- define urls ----
urlpatterns =[
    path('test/', views.working),
    path('show_articles', views.show_articles),

    #--- display wardrobe api list ---
    path('wardrobe/', views.ArticleList.as_view()),
    #--- display individual objects ---
    path('wardrobe/<int:pk>', views.ArticleDetail.as_view()),

    #--- protected routes ---
    path('wardrobe_protected/', views.ArticleListProtected.as_view())
]