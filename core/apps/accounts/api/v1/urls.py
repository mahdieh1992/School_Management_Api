from django.urls import path
from .views import UserRegisterApiView, UserViewSet, UserLoginView, ChangePasswordView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename="user")

app_name = 'users'
urlpatterns = [
    path("user/register/", UserRegisterApiView.as_view(), name= "register"),
    path("user/login/", UserLoginView.as_view(), name="login"),
    path("user/change_password/", ChangePasswordView.as_view(), name="change_password" )
]

urlpatterns += router.urls

