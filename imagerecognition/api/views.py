from rest_framework.response import Response
from rest_framework import viewsets, status

from . import serializers
from . import Task
from . import ImageRecognition


# Global variable used for the sake of simplicity.
# In real life, you'll be using your own interface to a data store
# of some sort, being caching, NoSQL, LDAP, external API or anything else
tasks = {
    # 1: Task(id=1, name='Demo', owner='xordoquy', status='Done'),
    # 2: Task(id=2, name='Model less demo', owner='xordoquy', status='Ongoing'),
    # 3: Task(id=3, name='Sleep more', owner='xordoquy', status='New'),
}


def get_next_task_id():
    return len(tasks) + 1

class TaskViewSet(viewsets.ViewSet):
    # print(f'TaskViewSet')
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = serializers.TaskSerializer

    def list(self, request):
        serializer = serializers.TaskSerializer(
            instance=tasks.values(), many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = serializers.TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            task.id = get_next_task_id()
            tasks[task.id] = task
            
            classifier = ImageRecognition.ImageRecognition(task.imagepath)
            ans = classifier.get_prediction()
            
            return Response({'result': ans}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)