from rest_framework import serializers
from staff_api.models.user import User


class CreateStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'salary']