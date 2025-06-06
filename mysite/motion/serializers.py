from rest_framework import serializers
from .models import *


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'


class HomeContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeContact
        fields = '__all__'


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'


class InfoCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoCard
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class ExamCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamCard
        fields = '__all__'


class ExamThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamTheme
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class VideoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoItem
        fields = '__all__'


class ClientContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContact
        fields = '__all__'



class MotionContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotionContact
        fields = '__all__'



class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'



class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'



class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = '__all__'


class CountryPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryPage
        fields = '__all__'


class CountryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryName
        fields = '__all__'


class ProgramTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramType
        fields = '__all__'


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CountryDescriptionCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryDescriptionCost
        fields = '__all__'


class CountryPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryPhoto
        fields = '__all__'


class CountryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryInfo
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class UniversityInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityInfo
        fields = '__all__'


class UniversityEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityEvent
        fields = '__all__'


class UniversityEventInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityEventInfo
        fields = '__all__'


class UniversityCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityCost
        fields = '__all__'


class UniversityPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityPhoto
        fields = '__all__'


class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields = '__all__'



