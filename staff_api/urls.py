from django.urls import path
from django.conf.urls import url
from staff_api.views.views import ListStaff, CreateStaff, StaffProfile
from rest_framework_swagger.views import get_swagger_view

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Staff Management System API",
      default_version='v1',
      description="A software for managing the activities of staff member is organizations",
      contact=openapi.Contact(email="hrfunsojoba@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', ListStaff.as_view(), name='list staff'),
    path('staff/create/', CreateStaff.as_view(), name='create staff'),
    path('profile/<str:pk>/', StaffProfile.as_view(), name='staff profile'),

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]