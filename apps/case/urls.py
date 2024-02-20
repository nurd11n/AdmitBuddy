from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CaseViewSet, AchievementsViewSet, EducationHistoryViewSet

routers = DefaultRouter()
routers.register("cases", CaseViewSet)
routers.register("achievements", AchievementsViewSet)
routers.register("education_historys", EducationHistoryViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]
