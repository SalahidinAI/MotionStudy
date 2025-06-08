from django.urls import path
from .views import *


urlpatterns = [
    path('home/', HomeAPIView.as_view(), name='home_list'),
    path('home_contact/', HomeContactAPIView.as_view(), name='home_contact_list'),
    path('home_info/', InfoAPIView.as_view(), name='home_info_list'),
    path('home_exam/', ExamAPIView.as_view(), name='home_exam_list'),
    path('home_videos/', VideoAPIView.as_view(), name='home_videos_list'),
    path('client_contact/', ClientContactAPIView.as_view(), name='client_contact_list'),
    path('motion_contact/', MotionContactAPIView.as_view(), name='motion_contact_list'),
    path('exam/<int:pk>/', ExamDetailAPIView.as_view(), name='exam_detail'),

    path('about/', AboutAPIView.as_view(), name='about_list'),
    path('team/', TeamAPIView.as_view(), name='team_list'),
    path('study/', StudyAPIView.as_view(), name='study_list'),
    path('country/', CountryPageAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country_detail'),
    path('country_info/<int:pk>/', CountryInfoAPIView.as_view(), name='country_info_detail'),

    path('university/', UniversityListAPIView.as_view(), name='university'),
    path('university_info/', UniversityInfoAPIView.as_view(), name='university_info'),
    path('university_event/', UniversityEventAPIView.as_view(), name='university_event'),

    path('university_event_info/<int:pk>/', UniversityEventInfoAPIView.as_view(), name='university_event_info'),
    path('university_cost/', UniversityCostAPIView.as_view(), name='university_cost'),
    path('university_photo/', UniversityPhotoAPIView.as_view(), name='university_photo'),

    # add ci/cd and deploy
]
