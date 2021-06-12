from rest_framework import serializers

from staff_api.models.supervisor import Supervisor


class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = ['name']
