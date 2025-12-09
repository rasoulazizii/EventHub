from rest_framework import viewsets, permissions
from .models import Category, Event
from .serializers import CategorySerializer, EventSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['category', 'organizer', 'status']
    search_fields = ['info', 'location', 'category__name']
    ordering_fields = ['start_date', 'created_at']
    ordering = ['-created_at']