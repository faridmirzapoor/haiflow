from rest_framework import serializers
from .models import Project, ProjectType
from customers.serializers import CustomerSerializer


class ProjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectType
        fields = ("id", "name")


class ProjectListSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    project_type = ProjectTypeSerializer(read_only=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "customer",
            "project_type",
            "price",
            "deadline",
            "progress",
            "priority",
        )


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "customer",
            "project_type",
            "price",
            "deadline",
            "progress",
            "priority",
        )
