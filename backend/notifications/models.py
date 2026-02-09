"""
مطابق دیاگرام: TNotification
"""
from django.db import models


class Notification(models.Model):
    """TNotification: اعلان."""

    title = models.CharField(max_length=255, db_column="ftitle")
    description = models.TextField(blank=True, db_column="fdescription")

    class Meta:
        db_table = "notifications_notification"

    def __str__(self):
        return self.title
