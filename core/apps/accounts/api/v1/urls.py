from django.urls import path
from .views import UserListView, UserDetailView

app_name = 'accounts'

urlpatterns = [
    path("accounts/", UserListView.as_view(),name="register"),
    path("accounts/<int:pk>/", UserDetailView.as_view(), name= "user_detail")
]
