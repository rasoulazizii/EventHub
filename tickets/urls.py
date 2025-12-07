from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketTypeViewSet, OrderViewSet

router = DefaultRouter()
router.register('ticket-types', TicketTypeViewSet)
router.register('orders', OrderViewSet, basename='orders')

urlpatterns = [
    path('', include(router.urls)),
]