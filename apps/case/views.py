from django.contrib.auth import get_user_model
from rest_framework import viewsets, status, filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsAdminPermission, IsAuthorPermission
from .models import Case, Achievements, EducationHistory
from .serializers import (CaseSerializer,
                          AchievementsSerializer,
                          EducationHistorySerializer,
                            CaseLisSerializer)
import django_filters


# Create your views here.

User = get_user_model()


class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, IsAdminPermission]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthorPermission]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()


    def get_serializer_class(self):
        if self.action == 'list':
            return CaseLisSerializer
        return self.serializer_class

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['first_name', "last_name", "gpa", "sat_act", "country"]
    search_fields = ['last_name', 'first_name', "gpa", "sat_act", "country"]
    ordering_fields = ['country', "gpa", "sat_act"]

class AchievementsViewSet(viewsets.ModelViewSet):
    queryset = Achievements.objects.all()
    serializer_class = AchievementsSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, IsAdminPermission]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthorPermission]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()


class EducationHistoryViewSet(viewsets.ModelViewSet):
    queryset = EducationHistory.objects.all()
    serializer_class = EducationHistorySerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, IsAdminPermission]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthorPermission]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()
