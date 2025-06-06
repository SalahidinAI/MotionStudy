from rest_framework import serializers
from .models import *


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['id', 'label', 'title', 'description', 'image1', 'image2', 'image3', 'image4']


class HomeContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeContact
        fields = ['name', 'phone_number']


class InfoCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoCard
        fields = ['id', 'title', 'description']


class InfoSerializer(serializers.ModelSerializer):
    info_cards = InfoCardSerializer(many=True, read_only=True)

    class Meta:
        model = Info
        fields = ['id', 'title', 'description', 'image', 'info_cards']


class ExamThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamTheme
        fields = ['id', 'theme', 'description']


class ExamCardSerializer(serializers.ModelSerializer):
    exam_card_themes = ExamThemeSerializer(many=True, read_only=True)

    class Meta:
        model = ExamCard
        fields = ['id', 'image1', 'image2', 'exam_type', 'title', 'exam_card_themes']


class ExamSerializer(serializers.ModelSerializer):
    exam_cards = ExamCardSerializer(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = ['id', 'title', 'description', 'exam_cards']


class VideoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoItem
        fields = ['id', 'videos']


class VideoSerializer(serializers.ModelSerializer):
    students_videos = VideoItemSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = ['id', 'title', 'students_videos']


class ClientContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContact
        fields = ['id', 'title']


class ClientContactCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContact
        fields = ['first_name', 'last_name', 'phone', 'email', 'organization', 'text']


class MotionContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotionContact
        fields = ['id', 'title', 'phone', 'email']


# continue here
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



