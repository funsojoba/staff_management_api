from django.shortcuts import render
from rest_framework.generics import (ListAPIView,
                                     ListCreateAPIView,
                                     RetrieveAPIView,
                                     CreateAPIView
                                     )
from .models import User, UserProfile
from .serializers import StaffSerializer, StaffProfileSerializer


class StaffView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = StaffSerializer


class RetrieveStaffView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = StaffSerializer


class StaffCreateView(RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = StaffProfileSerializer


class RegisterStaff(CreateAPIView):
    model = User
    serializer_class = StaffSerializer
