from django.db import router
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter # DefaultRouter includes a default API root view, that returns a 
#response containing hyperlinks to all the list views
#from .auth import obtain_auth_token
from .auth import CustomAuthToken

#creating Router Object 
router = DefaultRouter()

#register StudentViewSet with Router
router.register('studentdata', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('gettoken/', obtain_auth_token)
    path('gettoken/', CustomAuthToken.as_view())
]
