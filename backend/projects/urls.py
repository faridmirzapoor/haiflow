from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ProjectTypeViewSet

router = DefaultRouter()
router.register(r"types", ProjectTypeViewSet, basename="projecttype")
router.register(r"", ProjectViewSet, basename="project")

urlpatterns = [
    path("", include(router.urls)),
]
