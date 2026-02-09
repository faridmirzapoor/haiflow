"""
دسترسی استاندارد جنگو برای کل پروژه.
نقش کاربر از groups گرفته می‌شود؛ از Permission و user.has_perm() هم استفاده می‌شود.
"""
from rest_framework import permissions

from .models import User


class IsAdmin(permissions.BasePermission):
    """فقط کاربرانی که در گروه admin هستند."""

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_admin
        )


class IsActiveStudent(permissions.BasePermission):
    """فقط کاربران در گروه student با وضعیت فعال."""

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_student
            and request.user.status == User.Status.ACTIVE
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    """ادمین (گروه admin) هر کاری؛ بقیه فقط خواندن."""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_admin
        )


class DjangoModelPermission(permissions.BasePermission):
    """
    دسترسی بر اساس Permission استاندارد جنگو.
    نیاز به perm دارد؛ مثلاً: permission_required = 'api.view_blogpost'
    یا از get_permission_required() در ویو استفاده کنید.
    """

    def get_required_permission(self, request, view):
        if hasattr(view, "permission_required"):
            return view.permission_required
        if hasattr(view, "get_permission_required"):
            return view.get_permission_required(request)
        return None

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        perm = self.get_required_permission(request, view)
        if not perm:
            return True
        return request.user.has_perm(perm)

    def has_object_permission(self, request, view, obj):
        if not request.user or not request.user.is_authenticated:
            return False
        perm = self.get_required_permission(request, view)
        if not perm:
            return True
        # برای object-level: اگر مدل همان perm را دارد، چک کن
        return request.user.has_perm(perm)
