from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, filters
from .models import (UniversitiesFaculty,
                     Universities,
                     UniversitiesImage,
                     UniversitiesFacultyImage)
from .serializers import (UniversitiesSerializer,
                          UniversitiesFacultySerializer,
                          UniversitiesFacultyImageSerializer,
                          UniversitiesImageSerializer,
                          UniversitiesListSerializer)
from .permissions import IsAdminPermission
from rest_framework.permissions import AllowAny
import django_filters

# Create your views here.


class PermissionMixin:
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy', 'create'):
            permissions = [IsAdminPermission]
        else:
            permissions = [AllowAny]
        return [permissions() for permissions in permissions]


class UniversitiesViewSet(PermissionMixin, ModelViewSet):
    queryset = Universities.objects.all()
    serializer_class = UniversitiesSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return UniversitiesListSerializer
        return self.serializer_class

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['naming', "requirements"]
    search_fields = ['naming', "description", "requirements"]
    ordering_fields = ['naming']


class UniversitiesFacultyViewSet(PermissionMixin, ModelViewSet):
    queryset = UniversitiesFaculty.objects.all()
    serializer_class = UniversitiesFacultySerializer


class UniversitiesImageView(generics.CreateAPIView):
    queryset = UniversitiesImage.objects.all()
    serializer_class = UniversitiesImageSerializer
    permission_classes = [IsAdminPermission]


class UniversitiesFacultyImageView(generics.CreateAPIView):
    queryset = UniversitiesFacultyImage.objects.all()
    serializer_class = UniversitiesFacultyImageSerializer
    permission_classes = [IsAdminPermission]

