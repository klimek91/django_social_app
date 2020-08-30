from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('login/', views.user_login, name='login'),    poprzedni  widok login view
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    # dwa ponizsze adresy url sa przeznaczone do obslugi zmiany hasla
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]