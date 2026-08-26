from rest_framework.viewsets import ModelViewSet
from ...models import Practice
from .serializers import PracticeSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class PracticeViewSet(ModelViewSet):
    """ 
        Api end point for practice
    """
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name="Admin").exists():
            return Practice.objects.all()
        
        if user.groups.filter(name = "Teacher").exists():
            return Practice.objects.filter(created_by= user)
        
    def perform_create(self, serializer):
        practice = serializer.save(created_by= self.request.user)
        
