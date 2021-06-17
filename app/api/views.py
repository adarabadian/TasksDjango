import sys

from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import TaskSerializer
from .models import Task

# Create your views here.

#  #Decorator
#  @api_view(['GET'])
#  def tasklist(request):
#      tasks = Task.objects.all()
#      print(tasks)
#      serializer = TaskSerializer(tasks, many=True)
#      return Response(serializer.data)


from rest_framework.viewsets import GenericViewSet, mixins

#LIST MODEL MIXINS   -   FOR GET ALL() REQUESTS WHEN USING MODELS
#RetrieveModelMixin   -   FOR GET SPECIFIC REQUESTS
#RetrieveModelMixin   -   FOR GET WITH FILTER SPECIFIC REQUESTS

#UpdateModelMixin   -   FOR PATCH SPECIFIC ATTRIBUTE OF OBJECT

#CREATE MODEL MIXINS   -   FOR POST REQUESTS WHEN USING MODELS

#DestroyModelMixin   -   FOR DELETE PER ID

class TaskViewSet(GenericViewSet, mixins.ListModelMixin,
                  mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = TaskSerializer
    queryset = Task.objects.exclude(id=1)




