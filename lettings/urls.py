# Django Libs:
from django.urls import path
# Local Libs:
from . import views


app_name = "lettings"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
