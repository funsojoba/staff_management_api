from django.urls import path
from .views import StaffView, StaffCreateView, RetrieveStaffView, RegisterStaff


urlpatterns = [
    path('', StaffView.as_view(), name='home'),
    path('create-staff', RegisterStaff.as_view(), name='create-staff'),
    path('<int:pk>/', RetrieveStaffView.as_view(), name='staff'),
    path('staff-profile/<int:pk>/', StaffCreateView.as_view(), name='create')
]