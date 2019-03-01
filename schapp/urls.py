from django.urls import path
from . import views

app_name = 'schapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('departments/', views.departments, name='departments'),
    path('clubs/', views.clubs, name='clubs'),
    path('sports/', views.sports, name='sports'),


]