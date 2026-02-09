from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "status")
    list_filter = ("status", "groups")
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {"fields": ("phone_number", "status", "gender")}),
    )
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {"fields": ("phone_number", "status", "gender")}),
    )
