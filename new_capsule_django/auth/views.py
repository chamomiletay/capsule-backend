from .serializers import AuthSerializer
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model


#--- generate view that retrieves user information ---
class AuthUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthSerializer