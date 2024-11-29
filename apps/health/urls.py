from django.urls import path

from . import views

app_name = 'health'

urlpatterns = [
    path('', views.health_check, name='health_check'),
    path('server-time', views.server_time, name='server_time'),
]
