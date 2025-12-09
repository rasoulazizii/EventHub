from django.db import transaction
from rest_framework import viewsets, permissions, serializers
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
        ticket_type_input = serializer.validated_data['ticket_type']
        quantity = serializer.validated_data['quantity']
        
        with transaction.atomic():
            ticket = TicketType.objects.select_for_update().get(id=ticket_type_input.id)
            
            if ticket.capacity < quantity:
                raise serializers.ValidationError(
                    {"quantity": "Not enough tickets available. Someone just bought the last ones!"}
                )
            
            ticket.capacity -= quantity
            ticket.save()
            
            price = ticket.price
            total = price * quantity
            
            serializer.save(
                buyer=self.request.user,
                total_price=total,
                status='pai'
            )