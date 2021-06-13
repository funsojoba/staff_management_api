from django.shortcuts import render
from rest_framework import generics

from staff_api.models.user import User
from staff_api.models.profile import Profile
from staff_api.serializers.user_serializer import UserSerializer
from staff_api.serializers.create_staff_serializer import CreateStaffSerializer
from staff_api.serializers.user_profile_serializer import StaffProfileSerializer


class ListStaff(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateStaff(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateStaffSerializer


class StaffProfile(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = StaffProfileSerializer
