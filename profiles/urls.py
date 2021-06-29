# Django Libs:
from django.urls import path
# Local Libs:
from . import views


app_name = "profiles"
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]
