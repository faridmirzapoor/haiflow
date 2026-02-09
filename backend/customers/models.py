"""
مطابق دیاگرام: TCustomer
"""
from django.db import models


class Customer(models.Model):
    """TCustomer: مشتری."""

    first_name = models.CharField(max_length=255, db_column="ffname")
    last_name = models.CharField(max_length=255, db_column="flname")
    number = models.CharField(max_length=64, db_column="fnumber")

    class Meta:
        db_table = "customers_customer"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
