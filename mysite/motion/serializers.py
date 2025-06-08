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
        fields = ['id', 'image1', 'exam_type', 'title', 'exam_card_themes']


class ExamSerializer(serializers.ModelSerializer):
    exam_cards = ExamCardSerializer(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = ['id', 'title', 'description', 'exam_cards']


class ExamDetailSerializer(serializers.ModelSerializer):
    exam_themes = ExamThemeSerializer(many=True, read_only=True)

    class Meta:
        model = ExamCard
        fields = ['id', 'title', 'image2', 'exam_themes']


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


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'image', 'label', 'title', 'text', 'description']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'profile_image', 'name', 'info']


class TeamSerializer(serializers.ModelSerializer):
    team_members = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'title', 'team_members']


class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = ['id', 'title', 'study_image', 'description', 'bonus']


class CountryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryName
        fields = ['id', 'country_name']


class CountryListSerializer(serializers.ModelSerializer):
    location = CountryNameSerializer()

    class Meta:
        model = Country
        fields = ['id', 'flag1', 'location']


class CountryPageSerializer(serializers.ModelSerializer):
    countries = CountryListSerializer(many=True, read_only=True)

    class Meta:
        model = CountryPage
        fields = ['id', 'title', 'countries']


class ProgramTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramType
        fields = ['id', 'program']


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ['id', 'speciality_name']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class CountryDescriptionCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryDescriptionCost
        fields = ['id', 'description']


class CountryPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryPhoto
        fields = ['id', 'country_photos']


class CountryDetailSerializer(serializers.ModelSerializer):
    location = CountryNameSerializer(read_only=True)
    program_type = ProgramTypeSerializer(many=True, read_only=True)
    speciality = SpecialitySerializer(many=True, read_only=True)
    language = LanguageSerializer(many=True, read_only=True)
    country_descriptions = CountryDescriptionCostSerializer(many=True, read_only=True)
    country_photos = CountryPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'flag2', 'location', 'program_type', 'speciality', 'language',
                  'country_descriptions', 'country_photos']


class CountryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryInfo
        fields = ['id', 'title', 'information']


class CountryInfoDetailSerializer(serializers.ModelSerializer):
    country_info = CountryInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'country_info']


class CountrySimpleSerializer(serializers.ModelSerializer):
    location = CountryNameSerializer()
    class Meta:
        model = Country
        fields = ['location']


class UniversitySerializer(serializers.ModelSerializer):
    location = CountrySimpleSerializer()
    speciality = SpecialitySerializer(many=True)
    language = LanguageSerializer(many=True)
    program_type = ProgramTypeSerializer(many=True)

    class Meta:
        model = University
        fields = '__all__'


class UniversityInfoSerializer(serializers.ModelSerializer):
    university = UniversitySerializer()
    class Meta:
        model = UniversityInfo
        fields = ['id', 'university', 'title', 'information']


class UniversityEventSerializer(serializers.ModelSerializer):
    university = UniversitySerializer()

    class Meta:
        model = UniversityEvent
        fields = ['id', 'university', 'title', 'information']


class UniversityEventInfoSerializer(serializers.ModelSerializer):
    event = UniversityEventSerializer()
    class Meta:
        model = UniversityEventInfo
        fields = ['id', 'event', 'title', 'information']


class UniversityCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityCost
        fields = ['id', 'university', 'text', 'info']


class UniversityPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityPhoto
        fields = ['university', 'university_photos']


class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields = '__all__'



