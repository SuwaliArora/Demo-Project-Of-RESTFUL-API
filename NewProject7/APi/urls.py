from django.urls import path
from . import views

'''urlpatterns = [
    path('studentdata/', views.StudentListCreate.as_view()),
    #path('studentdata/<int:pk>', views.StudentRetrieve.as_view()),
    #path('studentdata/<int:pk>', views.StudentUpdate.as_view()),
    path('studentdata/<int:pk>', views.StudentRUD.as_view()),
]
'''
urlpatterns = [
    #path('studentdata/', views.StudentListCreate.as_view()),
    path('studentdata/', views.StudentList.as_view()),
]