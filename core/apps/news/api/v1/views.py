from rest_framework import generics
from ...models import News
from .serializers import NewsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class NewsView(generics.ListCreateAPIView):
    """ end point for retrieveing, updating and Deleting a model instance
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return News.objects.filter(class_room__teacher = self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(created_by= self.request.user)
            