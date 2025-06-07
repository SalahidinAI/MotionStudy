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

    # continue here
    # path(add ci/cd and deploy)
]
