# Django Libs:
from django.urls import path
# Local Libs:
from . import views


urlpatterns = [
	path('index/', views.index, name='index'),
]
