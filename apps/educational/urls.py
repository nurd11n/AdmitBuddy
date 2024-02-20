from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UniversitiesImageView,
                    UniversitiesFacultyViewSet,
                    UniversitiesFacultyImageView, UniversitiesViewSet)

routers = DefaultRouter()
routers.register("universities_faculty", UniversitiesFacultyViewSet)
routers.register("universities", UniversitiesViewSet)


urlpatterns = [
    path('', include(routers.urls)),
    path('add-universities-image/', UniversitiesImageView.as_view()),
    path('add-universities-faculty-image/', UniversitiesFacultyImageView.as_view()),
]