from django.urls import path
from . import views

#--- generate url for Create view
urlpatterns = [
    path('api/auth/signup/', views.AuthUserView.as_view())
]