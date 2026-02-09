# گروه‌های پیش‌فرض برای نقش کاربران (admin, student)

from django.db import migrations


def create_default_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    for name in ("admin", "student"):
        Group.objects.get_or_create(name=name)


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_remove_student_id_and_role"),
    ]

    operations = [
        migrations.RunPython(create_default_groups, noop),
    ]
