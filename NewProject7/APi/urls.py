from django.urls import path
from . import views

urlpatterns = [
    path('studentdata/', views.StudentList.as_view()),
]
