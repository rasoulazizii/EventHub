from rest_framework import viewsets, permissions
from .models import TicketType, Order
from .serializers import TicketTypeSerializer, OrderSerializer

class TicketTypeViewSet(viewsets.ModelViewSet):
    queryset = TicketType.objects.all()
    serializer_class = TicketTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

