from functools import partial
import json
import re
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student
 
@csrf_exempt
#view to extract serialized data as python data
def student_data(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)  #streamed data into python
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        #to convert python data into complex data
        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id') #id of the user whose data to be updated
        stu = Student.objects.get(id=id)
        #to convert python data into complex data
        serializer = StudentSerializer(stu, data = pythondata, partial=True) #partial=true is for telling we have to update only partial data
        # for complete data updation
        #serializer = StudentSerializer(stu, data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id') #id of the user whose data to be deleted
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data deleted'}
        #json_data = JSONRenderer().render(res)
        #return HttpResponse(json_data, content_type='application/json')
        # inplace of above 2 lines of code
        return JsonResponse(res, safe=True)
