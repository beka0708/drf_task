from django.urls import path
from .views import UserRegisterView, UserListView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="account_register"),
    path("account/", UserListView.as_view(), name="account_list"),
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
