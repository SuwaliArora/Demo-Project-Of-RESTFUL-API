from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from .pagination import PageNumberpagination, LimitoffsetPagination, cursorpagination

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = cursorpagination
    #pagination_class = LimitoffsetPagination
    #pagination_class = PageNumberpagination
    
 ''' 
    filter_backends = [OrderingFilter]
    #ordering_fields = ['city']    #order on the basis of city only
    ordering_fields = ['name', 'city']    #ordering on the basis of city or name
    #search_fields = ['^name']       # search on the basis of starting letter of name
   
    #filter_backends = [SearchFilter]
    #search_fields = ['city']    #search on the basis of city only
    #search_fields = ['name', 'city']    #search on the basis of city or name
    #search_fields = ['^name']       # search on the basis of starting letter of name
    
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['name', 'city']
    
    #filterset_fields = ['city']
    # to view data of a particular user using passby attribute
    #def get_queryset(self):
     #   user = self.request.user
     #   return Student.objects.filter(passby=user) 

'''
