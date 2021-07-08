from django.urls import path
from . import views

urlpatterns = [
    #path('studentdata/', views.student_data),
    #path('studentdata/<int:pk>', views.student_data),
    path('studentdata/', views.StudentAPI.as_view()),
    path('studentdata/<int:pk>', views.StudentAPI.as_view()),
]
