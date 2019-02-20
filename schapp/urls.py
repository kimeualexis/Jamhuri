from django.urls import path
from . import views

app_name = 'schapp'

urlpatterns = [
    path('', views.index, name='index'),
]
