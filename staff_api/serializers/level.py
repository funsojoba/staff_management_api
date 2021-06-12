from rest_framework import serializers

from staff_api.models.level import Level


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['name']
