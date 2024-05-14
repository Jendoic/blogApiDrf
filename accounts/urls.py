from django.urls import path
from .views import *

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("test/", TestApi.as_view(), name='test'),
    path("signup/", SignUpView.as_view(), name='signup'),
    path("logout/", LogOutView.as_view(), name='logout'),
    path("token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
]
