from social_network import views
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', views.SignUp),
    path('createPost/', views.createPost),
    path('login/', views.LoginToken.as_view(), name="Login"),
    # path('login/', obtain_auth_token, name="Login"),
    path('likePost/<int:id>/',views.likePost),
    path('unlikePost/<int:id>/',views.unlikePost),
    path('analitics/', views.analitics),
    path('lastLogin/', views.lastLogin),
    path('login/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
]