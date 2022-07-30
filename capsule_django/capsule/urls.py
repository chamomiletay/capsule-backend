#---- i m p o r t s ! ----
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
    path('wardrobe/', views.ViewArticle.as_view()),
    #--- display individual objects ---
    path('wardrobe/<int:pk>', views.ArticleDetail.as_view()),

    #--- protected routes ---
    path('wardrobe_protected/', views.ArticleListProtected.as_view()),
    path('wardrobe_protected/<int:pk>', views.ArticleDetailProtected.as_view()),
    path('random_outfit_protected/', views.NewOutfitProtected.as_view()),

    #--- user auth - test routes ---
    path('test_login', views.test_login),
    path('test_signup', views.test_signup),
]