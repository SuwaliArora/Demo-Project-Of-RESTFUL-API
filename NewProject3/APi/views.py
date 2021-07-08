from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView

#function based APIView

'''
@api_view(['GET','POST'])  #function based api view
def hello_world(request):
    if request.method == 'GET':
        return Response({ 'msg': 'This is GET Request'})

    if request.method == "POST":
        print(request.data)
        return Response({'msg':'this is post request', 'data':request.data})   #arguments in response method is python data primitive
'''

'''
@api_view(['GET','POST', 'PUT', 'PATCH', 'DELETE'])  #function based api view
def student_data(request, pk=None):
    if request.method == 'GET':
        #id = request.data.get('id')  #request.data has complete data in parsed form
        id = pk
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
            return Response({'msg':'Data created'}, status=status.HTTP_201_CREATED)   #response of data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        #id =  request.data.get('id')
        id=pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        #id =  request.data.get('id')
        id=pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'partial Data updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        #id =  request.data.get('id')
        id=pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})
'''

#class based APIView
class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data) #serialized data
        if serializer.is_valid():  #validation of data
            serializer.save()   
            return Response({'msg':'Data created'}, status=status.HTTP_201_CREATED)   #response of data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id=pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id=pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'partial Data updated'})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id=pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})
