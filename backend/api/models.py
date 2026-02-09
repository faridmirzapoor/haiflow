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


class BlogPost(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "انتظار"
        PENDING_APPROVAL = "pending_approval", "در انتظار تایید"
        PUBLISHED = "published", "منتشر شده"
        REJECTED = "rejected", "رد شده"
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    status = models.CharField(max_length=16, choices=Status.choices)
    published_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_read_count(self):
        return self.reads.count()


class BlogRead(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_reads")
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="reads")
    read_at = models.DateTimeField(auto_now_add=True)


class Resource(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    file = models.FileField(upload_to="resources/")
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name="resources")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Announcement(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "انتظار"
        PUBLISHED = "published", "منتشر شده"
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="announcements")
    status = models.CharField(max_length=9, choices=Status.choices)
    published_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Event(models.Model):
    class Type(models.TextChoices):
        EVENT = "event", "رویداد"
        WORKSHOP = "workshop", "ورکشاپ"
        CONTEST = "contest", "مسابقه"
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField(null=True)
    type = models.CharField(choices=Type.choices, max_length=8)
    capacity = models.IntegerField(null=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    location = models.CharField(max_length=255, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class EventRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_registrations")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="registrations")
    registered_at = models.DateTimeField(auto_now_add=True)