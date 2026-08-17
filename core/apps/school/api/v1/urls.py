from django.urls import path
from .views import SchoolViewSet, SchoolNearestListView, LessonViewSet, ClassRoomViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'schools', SchoolViewSet, basename="school")
router.register(r'lessons', LessonViewSet, basename="lesson")
router.register(r'classes', ClassRoomViewSet, basename= "classes")
urlpatterns = [
    path('schools/nearest/',SchoolNearestListView.as_view(), name="nearest" )
]
urlpatterns += router.urls
