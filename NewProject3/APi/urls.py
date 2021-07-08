from django.urls import path
from . import views

urlpatterns = [
    path('studentdata/', views.student_data),
    path('studentdata/<int:pk>', views.student_data),
]
