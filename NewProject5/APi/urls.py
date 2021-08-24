from django.db import router
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
# DefaultRouter includes a default API root view, that returns a 
#response containing hyperlinks to all the list views

#creating Router Object 
router = DefaultRouter()

#register StudentViewSet with Router
router.register('studentdata', views.StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]