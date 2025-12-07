from rest_framework import viewsets, permissions
from .models import TicketType, Order
from .serializers import TicketTypeSerializer, OrderSerializer

class TicketTypeViewSet(viewsets.ModelViewSet):
    queryset = TicketType.objects.all()
    serializer_class = TicketTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)

    def perform_create(self, serializer):
        ticket_type = serializer.validated_data['ticket_type']
        quantity = serializer.validated_data['quantity']
        price = ticket_type.price
        total = price * quantity
        
        serializer.save(
            buyer=self.request.user,
            total_price=total,
            status='pai'
        )