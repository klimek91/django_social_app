from django.urls import path
from . import views

urlpatterns = [
    #widok logowania
    path('login/', views.user_login, name='login'),
]