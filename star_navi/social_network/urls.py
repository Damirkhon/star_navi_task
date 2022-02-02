from social_network import views
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', views.SignUp),
    path('createPost/', views.createPost),
    path('login/', views.LoginToken.as_view(), name="Login"),
    # path('login/', obtain_auth_token, name="Login"),
    path('likePost/<int:id>/',views.likePost),
    path('unlikePost/<int:id>/',views.unlikePost),
    path('analitics/', views.analitics),
    path('lastLogin/', views.lastLogin),
]