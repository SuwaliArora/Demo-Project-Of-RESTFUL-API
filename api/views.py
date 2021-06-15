from rest_framework import serializers
from api.models import Student
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.

#model object - single student's data
def student_detail(request, pk):
    stu = Student.objects.get(id=pk)  #complex data
    serializer = StudentSerializer(stu)  # in python data
    #json_data = JSONRenderer().render(serializer.data) # to convert python data into json
    #return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

# query set - each student's data
def student_list(request):
    stu = Student.objects.all()  #complex data
    serializer = StudentSerializer(stu, many=True)  # in python data
    json_data = JSONRenderer().render(serializer.data) # to convert python data into json
    return HttpResponse(json_data, content_type='application/json')
    
