from rest_framework import serializers
from staff_api.models.user import User
from staff_api.models.profile import Profile
from .user_serializer import UserSerializer
from .department import DepartmentSerializer
from .designation import DesignationSerializer
from .level import LevelSerializer
from .supervisor import SupervisorSerializer


class StaffProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    department = DepartmentSerializer()
    designation = DesignationSerializer()
    level = LevelSerializer()
    supervisor = SupervisorSerializer()

    class Meta:
        model = Profile
        fields = ['user',
                  'phone',
                  'work_mail',
                  'state_of_origin',
                  'home_address',
                  'designation',
                  'department',
                  'supervisor',
                  'level']
        read_only_fields = ('designation', 'department', 'supervisor', 'salary', 'level')
