from django.urls import path
from . import views

urlpatterns = [
   # path('studentcreate/', views.student_create),
    path('studentdata/', views.student_data),
]
