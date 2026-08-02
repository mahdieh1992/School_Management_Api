from django.urls import path
from .views import UserListView, UserDetailView, LoginUserApi, LogoutUserApi

app_name = 'accounts'

urlpatterns = [
    path("accounts/", UserListView.as_view(),name="register"),
    path("accounts/<int:pk>/", UserDetailView.as_view(), name= "user_detail"),
    path("accounts/login/", LoginUserApi.as_view(), name="login_user"),
    path("accounts/logout/", LogoutUserApi.as_view(), name="logout_user")
]
