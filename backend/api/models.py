from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """نقش کاربر از طریق groups تعیین می‌شود (گروه‌های استاندارد جنگو)."""

    class Status(models.TextChoices):
        PENDING_ACTIVATION = "pending_activation", "در انتظار تایید"
        ACTIVE = "active", "فعال"
        SUSPENDED = "suspended", "مسدود شده"

    class Gender(models.TextChoices):
        MALE = "male", "مرد"
        FEMALE = "female", "زن"

    # نام گروه‌ها برای نقش (در auth.Group ساخته می‌شوند)
    GROUP_NAME_ADMIN = "admin"
    GROUP_NAME_STUDENT = "student"

    phone_number = models.CharField(max_length=11)
    status = models.CharField(max_length=18, choices=Status.choices)
    gender = models.CharField(max_length=6, choices=Gender.choices, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_admin(self):
        return self.groups.filter(name=self.GROUP_NAME_ADMIN).exists()

    @property
    def is_student(self):
        return self.groups.filter(name=self.GROUP_NAME_STUDENT).exists()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(null=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


