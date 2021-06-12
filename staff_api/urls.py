from django.urls import path
from .views import ListStaff, CreateStaff, StaffProfile


urlpatterns = [
    path('', ListStaff.as_view(), name='list staff'),
    path('staff/create/', CreateStaff.as_view(), name='create staff'),
    path('profile/<str:pk>/', StaffProfile.as_view(), name='staff profile')
]