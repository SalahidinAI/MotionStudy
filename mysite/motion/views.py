from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS
from .models import *
from .serializers import *
from rest_framework import filters
from rest_framework.permissions import SAFE_METHODS
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import UniversityFilter


class HomeAPIView(generics.ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class HomeContactAPIView(generics.CreateAPIView):
    queryset = HomeContact.objects.all()
    serializer_class = HomeContactSerializer


class InfoAPIView(generics.ListAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class ExamAPIView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ExamDetailAPIView(generics.RetrieveAPIView):
    queryset = ExamCard.objects.all()
    serializer_class = ExamDetailSerializer


class VideoAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class ClientContactAPIView(generics.ListCreateAPIView):
    queryset = ClientContact.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ClientContactListSerializer
        if self.request.method == 'POST':
            return ClientContactCreateSerializer


class MotionContactAPIView(generics.ListAPIView):
    queryset = MotionContact.objects.all()
    serializer_class = MotionContactSerializer


class AboutAPIView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class TeamAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class StudyAPIView(generics.ListAPIView):
    queryset = Study.objects.all()
    serializer_class = StudySerializer


class CountryPageAPIView(generics.ListAPIView):
    queryset = CountryPage.objects.all()
    serializer_class = CountryPageSerializer


class CountryDetailAPIView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer


class CountryInfoAPIView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryInfoDetailSerializer


class UniversityListAPIView(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversityListSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = [
        'location__location__country_name_en',
        'location__location__country_name_ru',
        'location__location__country_name_ky',
    ]
    filterset_class = UniversityFilter


class UniversityDetailAPIView(generics.RetrieveAPIView):
    queryset = University.objects.all()
    serializer_class = UniversityDetailSerializer


class ShareAPIView(generics.ListAPIView):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer


class UniversityDescriptionAPIView(generics.ListAPIView):
    queryset = UniversityInfo.objects.all()
    serializer_class = UniversityDescriptionSerializer


class UniversityEventAPIView(generics.ListAPIView):
    queryset = UniversityEvent.objects.all()
    serializer_class = UniversityEventSerializer


class UniversityCostAPIView(generics.ListAPIView):
    queryset = UniversityCost.objects.all()
    serializer_class = UniversityCostSerializer


class UniversityPhotoAPIView(generics.ListAPIView):
    queryset = UniversityPhoto.objects.all()
    serializer_class = UniversityPhotoSerializer


