"""
مطابق دیاگرام: TProject, TCustomerProject, TProjectContent, TSocialMediaTypes (ProjectType)
"""
from django.db import models


class ProjectType(models.Model):
    """TSocialMediaTypes: نوع پروژه / دسته‌بندی پروژه."""

    name = models.CharField(max_length=255, db_column="fname")

    class Meta:
        db_table = "projects_projecttype"

    def __str__(self):
        return self.name


class Project(models.Model):
    """TProject: پروژه."""

    customer = models.ForeignKey(
        "customers.Customer",
        on_delete=models.CASCADE,
        related_name="projects",
        db_column="fcustomer_id",
    )
    name = models.CharField(max_length=255, db_column="fname")
    project_type = models.ForeignKey(
        ProjectType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="projects",
        db_column="fproject_type_id",
    )
    price = models.BigIntegerField(default=0, db_column="fprice")
    deadline = models.DateField(null=True, blank=True, db_column="fdeadline")
    progress = models.PositiveSmallIntegerField(default=0, db_column="fprogress")
    priority = models.PositiveSmallIntegerField(default=0, db_column="fpriority")

    class Meta:
        db_table = "projects_project"

    def __str__(self):
        return self.name


class CustomerProject(models.Model):
    """TCustomerProject: ارتباط مشتری–پروژه (M2M)."""

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="customer_links",
        db_column="fproject_id",
    )
    customer = models.ForeignKey(
        "customers.Customer",
        on_delete=models.CASCADE,
        related_name="project_links",
        db_column="fcustomer_id",
    )

    class Meta:
        db_table = "projects_customerproject"
        unique_together = [("project", "customer")]

    def __str__(self):
        return f"{self.project.name} / {self.customer}"


class ProjectContent(models.Model):
    """TProjectContent: ارتباط پروژه–محتوا."""

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="content_links",
        db_column="fproject_id",
    )
    content = models.ForeignKey(
        "content.Content",
        on_delete=models.CASCADE,
        related_name="project_links",
        db_column="fcontent_id",
    )

    class Meta:
        db_table = "projects_projectcontent"
        unique_together = [("project", "content")]

    def __str__(self):
        return f"{self.project.name} / {self.content.title}"
