from rest_framework import viewsets, mixins, generics
from ...models import School, Lesson, ClassRoom
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import SchoolSerializer, NearestSchoolSerializer, LessonSerializer, ClassRoomSerializer
from geopy.distance import geodesic
from apps.accounts.models import Profile
from rest_framework.response import Response

class SchoolViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin, 
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,):

    """
        api for school 
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class SchoolNearestListView(generics.ListAPIView):
    """
        Calculate the distance to each school and return them sorted by proximity.
    """
    queryset = School.objects.all()
    serializer_class = NearestSchoolSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        profile = Profile.objects.get(user=request.user)
        user_cal = (profile.latitude, profile.longitude)
        for school in queryset:
            school_cal = (school.latitude, school.longitude)
            school.distance = geodesic(user_cal, school_cal).km
        queryset = sorted(queryset, key=lambda x: x.distance)
        serializer = self.get_serializer(queryset, many= True) 
        return Response(serializer.data)

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class ClassRoomViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,):
    
    """
        api endpoint for class_room
    """
    
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    

    
    