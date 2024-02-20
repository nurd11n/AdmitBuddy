from .models import Case, EducationHistory, Achievements
from rest_framework.serializers import ModelSerializer, ReadOnlyField
from django.contrib.auth import get_user_model

User = get_user_model()


class CaseLisSerializer(ModelSerializer):
    class Meta:
        model = Case
        fields = ["id", "first_name",
                  "last_name"]


class CaseSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')
    first_name = ReadOnlyField(source="user.first_name")
    last_name = ReadOnlyField(source="user.last_name")

    class Meta:
        model = Case
        fields = ["id", "user", "first_name",
                  "last_name", "gpa",
                  "sat_act", "ielts",
                  "toefl", "essay",
                  "country", "city"]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['achievements'] = AchievementsSerializer(instance.achievements_case.all(), many=True).data
        rep['education history'] = EducationHistorySerializer(instance.educ_history.all(), many=True).data
        return rep

    def create(self, validated_data):
        user = self.context['request'].user
        first_name = self.context['request'].user.first_name
        last_name = self.context['request'].user.last_name
        return self.Meta.model.objects.create(user=user,
                                              first_name=first_name,
                                              last_name=last_name,
                                              **validated_data)

    def update(self, instance, validated_data):
        User.objects.update(is_case_complete=True)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.gpa = validated_data.get('gpa', instance.gpa)
        instance.sat_act = validated_data.get('sat_act', instance.sat_act)
        instance.ielts = validated_data.get('ielts', instance.ielts)
        instance.toefl = validated_data.get('toefl', instance.toefl)
        instance.essay = validated_data.get('essay', instance.essay)
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance


class AchievementsSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')
    case = ReadOnlyField(source="case.first_name")

    class Meta:
        model = Achievements
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        case = self.context['request'].user.case
        return self.Meta.model.objects.create(user=user, case=case, **validated_data)


class EducationHistorySerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')
    case = ReadOnlyField(source="case.first_name")

    class Meta:
        model = EducationHistory
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        case = self.context.get('request').user.case
        return self.Meta.model.objects.create(user=user, case=case, **validated_data)
