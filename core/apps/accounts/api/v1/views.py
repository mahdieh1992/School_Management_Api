from rest_framework import generics
from django.contrib.auth import get_user_model, authenticate
from .serializers import UserRegisterSerializer, UserSerializer, UserLoginSerializer, ChangPasswordSerializer
from rest_framework.permissions import AllowAny
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()

class UserRegisterApiView(generics.CreateAPIView):
    """ Api endpoint for user registeration

    Method:
        POST: Create a new user account.
    """
    serializer_class = UserRegisterSerializer
    permission_classes= [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data= request.data)
        serializer.is_valid(raise_exception= True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data['token']= {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_201_CREATED)
        
    
class UserViewSet(mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,):
    
    """ 
        ViewSet for listing or retrieving users.
    method:
        get, put,partial_update, delete
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            "user": serializer.data, 
            "message": "User Retrieve successfully"},
            status= status.HTTP_200_OK)
   
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if "email" in request.data:
            return Response(
                {"message": "You cannot change your email"},
                status= status.HTTP_400_BAD_REQUEST
            )
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid(raise_exception= True):
            self.perform_update(serializer)
            return Response({
                "message": "Update user successfully"
            }, status= status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        response= Response(status= status.HTTP_204_NO_CONTENT)
        response['X-Message']= "User deleted successfully"
        return response
    
class UserLoginView(generics.GenericAPIView):
    """ 
        Login user with jwt token
    """
    serializer_class = UserLoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception= True)
        user = serializer.validated_data
        data = serializer.data
        token = RefreshToken.for_user(user)
        data['token']= {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_200_OK)
    
class ChangePasswordView(generics.UpdateAPIView):
    """
        Update API for changing user's password.
    """
    serializer_class = ChangPasswordSerializer
    permission_classes = [IsAuthenticated]
    def update(self, request, *args, **kwargs):
        instance = self.request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception= True)
        instance.set_password(serializer.validated_data["new_password"])
        instance.save()
        return Response({"message":"Password updated successfully"}, status= status.HTTP_200_OK)
    
class LogoutUserView(APIView):
    """
        Api endpoint for logout users
    """
    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status= status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)