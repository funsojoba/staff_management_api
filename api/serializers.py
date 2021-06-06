from rest_framework import serializers
from .models import User, UserProfile, Supervisor, Designation, Department


class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = ['name']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name']


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = ['name']


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

        extra_kwargs = {"password": {
            "write_only": True,
            "required": True
        }}


class StaffProfileSerializer(serializers.ModelSerializer):
    user = StaffSerializer()
    designation = DesignationSerializer()
    department = DepartmentSerializer()
    supervisor = SupervisorSerializer()

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

