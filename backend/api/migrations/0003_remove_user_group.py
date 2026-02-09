# حذف ستون group از User (ساختار دسترسی سفارشی حذف شد؛ دسترسی استاندارد جنگو)

from django.db import connection, migrations


def drop_group_column(apps, schema_editor):
    with connection.cursor() as cursor:
        if connection.vendor == "postgresql":
            cursor.execute("ALTER TABLE api_user DROP COLUMN IF EXISTS fgroup_id;")
        else:
            try:
                cursor.execute("ALTER TABLE api_user DROP COLUMN fgroup_id;")
            except Exception:
                pass  # ستون قبلاً حذف شده یا وجود ندارد


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_user_group_alter_user_gender"),
    ]

    operations = [
        migrations.RunPython(drop_group_column, noop),
    ]
