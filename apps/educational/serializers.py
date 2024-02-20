from rest_framework.serializers import ModelSerializer
from .models import UniversitiesFaculty, Universities, UniversitiesImage, UniversitiesFacultyImage


class UniversitiesListSerializer(ModelSerializer):
    class Meta:
        model = Universities
        fields = ["id", "naming"]


class UniversitiesSerializer(ModelSerializer):
    class Meta:
        model = Universities
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['images'] = UniversitiesImageSerializer(instance.images.all(), many=True).data
        rep['Faculty'] = UniversitiesFacultySerializer(instance.universities_faculty.all(), many=True).data
        return rep


class UniversitiesFacultySerializer(ModelSerializer):
    class Meta:
        model = UniversitiesFaculty
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['images'] = UniversitiesFacultyImageSerializer(instance.images.all(), many=True).data
        return rep


class UniversitiesImageSerializer(ModelSerializer):
    class Meta:
        model = UniversitiesImage
        fields = "__all__"


class UniversitiesFacultyImageSerializer(ModelSerializer):
    class Meta:
        model = UniversitiesFacultyImage
        fields = "__all__"
