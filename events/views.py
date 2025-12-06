from rest_framework import viewsets, permissions
from .models import Category, Event
from .serializers import CategorySerializer, EventSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]