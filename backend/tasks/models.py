"""
مطابق دیاگرام: TTask, TContentTask
"""
from django.conf import settings
from django.db import models


class Task(models.Model):
    """TTask: وظیفه."""

    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        related_name="tasks",
        db_column="fproject_id",
    )
    name = models.CharField(max_length=255, db_column="fname")
    description = models.TextField(blank=True, db_column="fdescription")
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_tasks",
        db_column="fassignee",
    )
    deadline = models.DateField(null=True, blank=True, db_column="fdeadline")
    priority = models.PositiveSmallIntegerField(default=0, db_column="fpriority")
    estimate = models.PositiveSmallIntegerField(default=0, db_column="festimate")

    class Meta:
        db_table = "tasks_task"

    def __str__(self):
        return self.name


class ContentTask(models.Model):
    """TContentTask: ارتباط محتوا–وظیفه."""

    content = models.ForeignKey(
        "content.Content",
        on_delete=models.CASCADE,
        related_name="task_links",
        db_column="fcontent_id",
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="content_links",
        db_column="ftask_id",
    )

    class Meta:
        db_table = "tasks_contenttask"
        unique_together = [("content", "task")]

    def __str__(self):
        return f"{self.content.title} / {self.task.name}"
