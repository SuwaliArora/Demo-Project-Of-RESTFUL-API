from django.urls import path
from django.urls.conf import path, include
from . import views
from rest_framework.routers import DefaultRouter

#creating Router Object 
router = DefaultRouter()

#register SingerViewSet and SongViewSet with Router
router.register('singer', views.SingerViewSet, basename='singer')
router.register('song', views.SongViewSet, basename='song')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
