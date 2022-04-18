from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from users import models, serializers


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return models.User.objects.filter(created_by=self.request.user).all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
