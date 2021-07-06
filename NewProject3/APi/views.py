from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

'''
@api_view(['GET','POST'])  #function based api view
def hello_world(request):
    if request.method == 'GET':
        return Response({ 'msg': 'This is GET Request'})

    if request.method == "POST":
        print(request.data)
        return Response({'msg':'this is post request', 'data':request.data})   #arguments in response method is python data primitive
'''

@api_view(['GET','POST', 'PUT', 'DELETE'])  #function based api view
def student_data(request):
    if request.method == 'GET':
        id = request.data.get('id')  #request.data has complete data in parsed form
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = StudentSerializer(data=request.data) #serialized data
        if serializer.is_valid():  #validation of data
            serializer.save()   
            return Response({'msg':'Data created'})   #response of data
        return Response(serializer.errors)
    
    if request.method == 'PUT':
        id =  request.data.get('id')
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id =  request.data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})
        
