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
    path('working/', views.working),
    path('show_articles', views.show_articles),
]