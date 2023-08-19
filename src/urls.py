from django.contrib import admin
from django.urls import path
from .views import *

from rest_framework.routers import DefaultRouter
from .views import ElevatorSystemViewSet, ElevatorViewSet

router = DefaultRouter()
router.register(r'system', ElevatorSystemViewSet, basename='system')

urlpatterns = [
    path('system/<int:pk>/show_elevators/', ElevatorSystemViewSet.as_view({'get': 'show_elevators'}), name='elevator-system-show-elevators'),
    path('system/<int:id>/elevator/<int:pk>/', ElevatorViewSet.as_view({'get': 'show', 'put': 'custom_update', 'patch': 'custom_update'}), name='elevator-show'),
    path('system/<int:id>/elevator/<int:pk>/make_request/', ElevatorViewSet.as_view({'post': 'make_request'}), name='elevator-make-request'),
    path('system/<int:id>/elevator/<int:pk>/destination/', ElevatorViewSet.as_view({'get': 'destination'}), name='elevator-destination'),
    path('system/<int:id>/elevator/<int:pk>/req_current_status/', ElevatorViewSet.as_view({'get': 'req_current_status'}), name='elevator-req-current-status'),
] + router.urls

