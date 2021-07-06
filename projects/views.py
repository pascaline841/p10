from rest_framework import permissions, viewsets

from .models import Project
from .permissions import IsProjectAuthor, IsProjectContributor
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """API endpoint that allows projects to be viewed or edited."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsProjectAuthor,
        IsProjectContributor,
    ]

    def get_queryset(self, *args, **kwargs):
        return Project.objects.filter(author_user=self.request.user)
