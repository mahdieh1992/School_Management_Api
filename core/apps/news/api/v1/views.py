from rest_framework import generics, viewsets
from ...models import News, NewsReceiver
from ....school.models import ClassRoom
from .serializers import NewsSerializer, NewsReceiverSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.response import Response

User = get_user_model()
class NewsViewSet(viewsets.ModelViewSet):
    """ end point for create, list a model instance
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return News.objects.filter(class_room__teacher = self.request.user)
    
    def perform_create(self, serializer):
        get_class =  serializer.validated_data['class_room']
        new = serializer.save(created_by= self.request.user)
        
        for student in get_class.student.all():
            NewsReceiver.objects.create(
                news=new,
                student=student,
                is_read=0,
                read_date=None)      
   
class NewsReceiverView(generics.ListAPIView):
    """ End point show news for students
    """
    queryset = NewsReceiver.objects.all()
    serializer_class = NewsReceiverSerializer
    permission_classes = [IsAuthenticated]
 
    def get_queryset(self):
        return NewsReceiver.objects.filter(student= self.request.user)
    
class NewsReciverRetrieveView(generics.RetrieveAPIView):
    """
        Endpoint for retrieving news receiver details.
    """
    queryset = NewsReceiver.objects.all()
    serializer_class = NewsReceiverSerializer
    permission_classes = [IsAuthenticated]
    
    def retrieve(self, request, *args, **kwargs):
        news_receiver = self.get_object()
        
        if not news_receiver.is_read:
            news_receiver.is_read = True
            news_receiver.read_date = timezone.now()
            news_receiver.save(update_fields=["is_read", "read_date"])

        serializer = self.get_serializer(news_receiver)
        return Response(serializer.data)
       