from rest_framework import serializers
from .models import TicketType, Order

class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['id', 'buyer', 'total_price', 'status', 'created_at', 'updated_at']

    def validate(self, attrs):
        ticket_type = attrs['ticket_type']
        quantity = attrs['quantity']

        if ticket_type.capacity < quantity:
            raise serializers.ValidationError({"quantity": "Not enough tickets available."})
        
        return attrs