from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from .models import User, UserProfile
from .serializers import StaffSerializer, StaffProfile


class StaffView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = StaffSerializer


class StaffCreateView(RetrieveAPIView):
    queryset = UserProfile
    serializer_class = StaffProfile


