from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),  # URL pattern for the home page



]
