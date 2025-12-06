from django.db import models
from django.contrib.auth import get_user_model
from core.models import AbstractModel
from events.models import Event

User = get_user_model()

class TicketType(AbstractModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='ticket_type')
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    capacity = models.PositiveIntegerField()
    sales_start = models.DateTimeField()
    sales_end = models.DateTimeField()

    def __str__(self):
        return self.name


class Order(AbstractModel):
    CHOICES = [
        ['pen', 'Pendigs'],
        ['pai', 'Paid'],
        ['can', 'Cancelled'],
        ['exp', 'Expired']
    ]
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ticket_type = models.ForeignKey(TicketType, on_delete=models.PROTECT, related_name='orders')
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=5, choices=CHOICES, default='pen')


