from rest_framework import serializers
from .models import TicketType, Order

class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = '__all__'

