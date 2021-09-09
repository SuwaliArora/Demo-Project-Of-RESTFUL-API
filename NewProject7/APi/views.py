from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #filterset_fields = ['name', 'city']
    filter_backends = [SearchFilter]
    search_fields = ['city']    #search on the basis of city only
    #search_fields = ['name', 'city']    #search on the basis of city or name
    #search_fields = ['^name']       # search on the basis of starting letter of name
