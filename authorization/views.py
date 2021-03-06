from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import RegistrationSerializer
from rest_framework.permissions import AllowAny
# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer
