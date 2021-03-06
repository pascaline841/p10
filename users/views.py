from django.contrib.auth.models import User

from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreateUserView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        author = request.data
        serializer = UserSerializer(data=author)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
