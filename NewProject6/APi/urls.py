from django.db import router
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter # DefaultRouter includes a default API root view, that returns a 
#response containing hyperlinks to all the list views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

#creating Router Object 
router = DefaultRouter()

#register StudentViewSet with Router
router.register('studentdata', views.StudentModelViewSet, basename='student')

'''urlpatterns = [
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
]
'''

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
