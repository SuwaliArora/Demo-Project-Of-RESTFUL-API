from rest_framework import serializers
from api.models import Student
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.

#model object - single student data
def student_detail(request):
    stu = Student.objects.get(id=2)  #complex data
    print(stu)
    serializer = StudentSerializer(stu)  # in python data
    print(serializer)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data) # to convert python data into json
    print(json_data)
    return HttpResponse(json_data, content_type='application/json')
