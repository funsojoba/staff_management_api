from rest_framework import serializers
from .models import User, UserProfile


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class StaffProfile(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'user',
            'date_of_birth',
            'phone_number',
            'supervisor',
            'state_of_origin',
            'designation',
            'department'
        ]
