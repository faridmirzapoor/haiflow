from rest_framework import serializers
from .models import Order
from api.serializers import UserSerializer


class OrderSerializer(serializers.ModelSerializer):
    sender_detail = UserSerializer(source="sender", read_only=True)
    receiver_detail = UserSerializer(source="receiver", read_only=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "sender",
            "sender_detail",
            "receiver",
            "receiver_detail",
            "title",
            "description",
        )
        extra_kwargs = {"sender_detail": {"read_only": True}, "receiver_detail": {"read_only": True}}
