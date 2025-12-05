from django.db import models
from django.contrib.auth import get_user_model
from core.models import AbstractModel

User = get_user_model()

class Category(AbstractModel):
    name = models.CharField(max_length=70)
    parent = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        related_name='children',
        null=True,
        blank=True
    )
    def __str__(self):
        return self.name

class Event(AbstractModel):
    CHOICES = [
        ['d', 'Draft'],
        ['p', 'Published'],
        ['c', 'canceled'],
    ]
    organizer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='organizer')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='Event')
    info = models.TextField()
    start_dates = models.DateTimeField()
    end_dates = models.DateTimeField()
    location = models.CharField(max_length=220)
    status = models.CharField(max_length=1, choices=CHOICES, default='d')

    def __str__(self):
        return self.info

