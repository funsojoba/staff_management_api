from django.urls import path
from .views import ListStaff


urlpatterns = [
    path('', ListStaff.as_view(), name='List Staff')
]