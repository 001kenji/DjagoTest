from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.Home, name='Home'),
    path('user', views.User, name='User')
]

