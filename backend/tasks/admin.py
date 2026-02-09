from django.contrib import admin
from .models import ContentTask, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "project", "assignee", "deadline", "priority", "estimate")
    list_filter = ("project",)


@admin.register(ContentTask)
class ContentTaskAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "task")
