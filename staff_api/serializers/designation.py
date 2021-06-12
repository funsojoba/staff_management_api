from rest_framework import serializers

from staff_api.models.designation import Designation


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = ['name']
