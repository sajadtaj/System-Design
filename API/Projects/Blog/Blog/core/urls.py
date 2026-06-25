from django.contrib import admin
from django.urls import path,include
from drf_spectacular.views import (
        SpectacularAPIView,          # For Schema
        SpectacularRedocView,        # For Docs
        SpectacularSwaggerView,      # For Swagger
        )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('posts.urls')),
    path("api-auth",include('rest_framework.urls')),
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")),                           # for login,logout,reset pass
    path("api/v1/dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")), # for register
    path("api/schema/",SpectacularAPIView.as_view(),name="schema"),
    path("api/docs/", SpectacularRedocView.as_view(url_name="schema"), name="docs"),
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),

]
