from django.urls import path
from .views import NewsViewSet,NewsReceiverView, NewsReciverRetrieveView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'news', NewsViewSet, basename="news")

urlpatterns = [
    path("news/news_receiver/", NewsReceiverView.as_view(), name="news_receiver"),
    path("news/news_receiver/<int:pk>/",NewsReciverRetrieveView.as_view(), name="new_retrieve")
]

urlpatterns +=router.urls