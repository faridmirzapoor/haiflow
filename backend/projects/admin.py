from django.contrib import admin
from .models import CustomerProject, Project, ProjectContent, ProjectType


@admin.register(ProjectType)
class ProjectTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "customer", "project_type", "price", "deadline", "progress", "priority")
    list_filter = ("project_type",)


@admin.register(CustomerProject)
class CustomerProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "customer")


@admin.register(ProjectContent)
class ProjectContentAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "content")
