from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS
from .models import *
from .serializers import *
from rest_framework import filters
from rest_framework.permissions import SAFE_METHODS


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


# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer