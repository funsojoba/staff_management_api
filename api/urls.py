from django.urls import path
from .views import StaffView, StaffCreateView


urlpatterns = [
    path('', StaffView.as_view(), name='home'),
    path('staff-profile/<int:pk>/', StaffCreateView.as_view(), name='create')
]