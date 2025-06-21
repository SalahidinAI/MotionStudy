# filters.py
import django_filters
from .models import University

class UniversityFilter(django_filters.FilterSet):
    location = django_filters.CharFilter(method='filter_by_multilang_location')

    def filter_by_multilang_location(self, queryset, name, value):
        return queryset.filter(
            models.Q(location__location__country_name_en__icontains=value) |
            models.Q(location__location__country_name_ru__icontains=value) |
            models.Q(location__location__country_name_tr__icontains=value)
        )

    class Meta:
        model = University
        fields = ['location']
