from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserListView, UserCreateView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListView.as_view(), name='custom_user_list'),
    path('create/', UserCreateView.as_view(), name='custom_user_create'),

    # authorization urls
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]