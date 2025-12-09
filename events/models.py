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
    class Status(models.TextChoices):
        DRAFT = 'd', 'Draft'
        PUBLISHED = 'p', 'Published'
        CANCELED = 'c', 'Canceled'

    organizer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='organized_events')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='events')
    info = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()  
    location = models.CharField(max_length=220)
    
    status = models.CharField(
        max_length=1, 
        choices=Status.choices, 
        default=Status.DRAFT
    )

    def __str__(self):
        return self.info