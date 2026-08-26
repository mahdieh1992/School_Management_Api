from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PracticeViewSet

router = DefaultRouter()
router.register("practice", PracticeViewSet, basename="practice" )

urlpatterns = [
]

urlpatterns +=router.urls