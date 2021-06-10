from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi
from django.contrib import admin 
from django.urls import path , include
from rest_framework import permissions
from rest_framework.authtoken import views

schema_view = get_schema_view(
openapi.Info(
title="Admin Panel",
default_version="v1",
description="test for madtalk admin",
terms_of_service="https://www.google.com/policies/terms/",
contact=openapi.Contact(email="hello@example.com"),
license=openapi.License(name="BSD License"),
),
public=True,
permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/',views.obtain_auth_token),
    path('question-bank/', include('question_bank.urls')),
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),
]
