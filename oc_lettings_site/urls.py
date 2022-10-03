from django.contrib import admin
from django.urls import path, include

from . import views


def trigger_error(request):
    return 1 / 0


urlpatterns = [
    path("", views.index, name="home"),
    path("admin/", admin.site.urls),
    path("", include("lettings.urls")),
    path("", include("profiles.urls")),
    path("sentry-debug/", trigger_error),
]
