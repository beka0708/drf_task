from django.contrib import admin
from django.urls import path, include
from . import swagger

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("apps.user.urls")),
    path("api/portal/", include("apps.portal.urls")),
]

urlpatterns += swagger.urlpatterns
