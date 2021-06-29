# Django Libs:
from django.contrib import admin
from django.urls import path, include
# Local Libs:
from . import views


def trigger_error(request):
    """Just there to show error events on sentry"""
    division_by_zero = 1 / 0  # noqa: F841


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),  # Only there to show error events
]
