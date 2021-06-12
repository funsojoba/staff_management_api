from rest_framework import serializers

from staff_api.models.department import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name']
