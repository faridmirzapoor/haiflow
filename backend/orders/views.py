from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """API for Orders (ابلاغیه)."""

    queryset = Order.objects.select_related("sender", "receiver").all()
    serializer_class = OrderSerializer
