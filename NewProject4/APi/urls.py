from django.urls import path
from . import views

urlpatterns = [
    path('studentdata/', views.StudentListCreate.as_view()),
    path('studentdata/<int:pk>', views.StudentRUD.as_view()),
]
