import django_filters
from .models import University

class UniversityFilter(django_filters.FilterSet):
    location = django_filters.CharFilter(method='filter_by_multilang_location')

    class Meta:
        model = University
        fields = ['location']
