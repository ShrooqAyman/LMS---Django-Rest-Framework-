from .views import RegisterAPI,LoginAPI
from django.urls import path
from . import views
from knox import views as knox_views

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('', views.SignUp, name="SignUp"),
    path('dashboard', views.Dashboard, name="Dashboard"),
    path('login', views.Logins, name="Logins"),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]