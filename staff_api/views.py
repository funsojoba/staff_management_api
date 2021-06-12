from django.shortcuts import render
from rest_framework import generics
from staff_api.models.user import User
from staff_api.serializers.user_serializer import UserSerializer


class ListStaff(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

