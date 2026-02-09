"""
مطابق دیاگرام: TOrder (سفارش/درخواست با فرستنده و گیرنده)
"""
from django.conf import settings
from django.db import models


class Order(models.Model):
    """TOrder: سفارش/درخواست."""

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_orders",
        db_column="fsender_id",
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="received_orders",
        db_column="freceiver_id",
    )
    title = models.CharField(max_length=255, db_column="ftitle")
    description = models.TextField(blank=True, db_column="fdescription")

    class Meta:
        db_table = "orders_order"

    def __str__(self):
        return self.title
