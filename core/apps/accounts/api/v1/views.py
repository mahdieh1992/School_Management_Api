from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegisterationSerializer, UserSerializer
from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .serializers import LoginUserSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class UserListView(APIView):
    """ 
        List all user and create new user
    """
    serializer_class = UserRegisterationSerializer
    
    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)
    
      
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many= True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"User Registered successfull"},
                status=status.HTTP_201_CREATED
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

class UserDetailView(APIView):
    """ 
        Retrieve Update Delete for a user instance
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk = pk)
        except User.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        user = self.get_object(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk):
        user = self.get_object(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        user = self.get_object(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class LoginUserApi(APIView):
    """ 
        Login users with TokenAuthentication
    """
    serializer_class = LoginUserSerializer
    authentication_classes = [TokenAuthentication]
    
    def post(self, request, *args, **kwargs):
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = authenticate(username=serializer.data['username'],password=serializer.data['password'])
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'Token': [token.key], 'detail': 'Login User Successfully'})
            return Response({"Message":"Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LogoutUserApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)