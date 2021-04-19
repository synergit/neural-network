from rest_framework import serializers
from . import Task

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imagepath = serializers.CharField()
    def create(self, validated_data):
        return Task(id=None, **validated_data)
