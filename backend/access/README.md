# اپ access حذف شده

ساختار دسترسی سفارشی (TGroup, TAccess, TGroupAccess) حذف شده است.

از **دسترسی استاندارد جنگو** استفاده کنید:

- **Group** و **Permission**: `django.contrib.auth.models.Group`, `Permission`
- کاربران با **User.groups** و **User.user_permissions** مدیریت می‌شوند
- در ویوها: `request.user.has_perm('app_label.permission_codename')`
- در DRF: از `api.permissions.DjangoModelPermission` یا `rest_framework.permissions.DjangoModelPermissions` استفاده کنید

این پوشه برای سازگاری با مایگریشن‌های قبلی نگه داشته شده و می‌توانید آن را حذف کنید.
