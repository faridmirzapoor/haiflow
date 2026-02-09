"""
مطابق دیاگرام: TContent
"""
from django.db import models


class Content(models.Model):
    """TContent: محتوا."""

    title = models.CharField(max_length=255, db_column="ftitle")
    is_uploaded = models.BooleanField(default=False, db_column="fis_uploaded")
    published_date = models.DateField(null=True, blank=True, db_column="fpublished_date")
    tags = models.JSONField(null=True, blank=True, db_column="ftags")

    class Meta:
        db_table = "content_content"

    def __str__(self):
        return self.title
