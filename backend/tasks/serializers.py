from rest_framework import serializers
from .models import Task
from api.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    assignee_detail = UserSerializer(source="assignee", read_only=True)

    class Meta:
        model = Task
        fields = (
            "id",
            "project",
            "name",
            "description",
            "assignee",
            "assignee_detail",
            "deadline",
            "priority",
            "estimate",
        )
        extra_kwargs = {"assignee_detail": {"read_only": True}}
