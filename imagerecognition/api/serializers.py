from rest_framework import serializers
from . import Task


# STATUSES = (
#     'New',
#     'Ongoing',
#     'Done',
# )


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imagepath = serializers.CharField()
    # owner = serializers.CharField(max_length=256)
    # status = serializers.ChoiceField(choices=STATUSES, default='New')

    def create(self, validated_data):
        # print(f'TaskSerializer, create() - {validated_data}')
        return Task(id=None, **validated_data)

    # def update(self, instance, validated_data):
    #     for field, value in validated_data.items():
    #         setattr(instance, field, value)
    #     return instance