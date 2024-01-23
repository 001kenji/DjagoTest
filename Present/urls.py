from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.Home),
    path('user', views.User)
]

