from rest_framework import viewsets
from .models import Project, ProjectType
from .serializers import ProjectSerializer, ProjectListSerializer, ProjectTypeSerializer


class ProjectTypeViewSet(viewsets.ModelViewSet):
    queryset = ProjectType.objects.all()
    serializer_class = ProjectTypeSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.select_related("customer", "project_type").all()
    serializer_class = ProjectListSerializer

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return ProjectSerializer
        return ProjectListSerializer
