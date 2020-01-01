from django.contrib import admin
from django.urls import path,include
from app_1 import views 

app_name = "app_1"

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]
