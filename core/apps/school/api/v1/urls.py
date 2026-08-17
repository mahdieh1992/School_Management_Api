from django.urls import path
from .views import SchoolViewSet, NearestSchoolView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'schools', SchoolViewSet, basename="school")

urlpatterns = [
    path('schools/nearest/',NearestSchoolView.as_view(), name="nearest" )
]
urlpatterns += router.urls
