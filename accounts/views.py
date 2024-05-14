from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import *
from rest_framework.views import APIView
from rest_framework import generics, status, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import *
from .models import *


class TestApi(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def get(self, request, *args, **kwargs):
        print(request.user)
        return Response({"detail":"User is Authenticated!" })
    
    
class SignUpView(generics.GenericAPIView):
    
    def post(self, request):
        serializers = UserSerializer(data=request.data)
        
        data = {}
        
        if serializers.is_valid():
            account = serializers.save()
            
            data['email'] = account.email
            data['username'] = account.username
            data['response'] = "Registration successful"
            
        else:
            data = serializers.errors
        
        return Response(data=data)
    
    
class LogOutView(APIView):
    
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    