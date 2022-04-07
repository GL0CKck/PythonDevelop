from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("main/", include("mainapp.urls", namespace="mainapp")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
