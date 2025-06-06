from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class GeneralMedia:
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Home)
class HomeAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(Info)
class InfoAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(InfoCard)
class InfoCardAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(Exam)
class ExamAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(ExamCard)
class ExamCardAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(ExamTheme)
class ExamThemeAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(Video)
class VideoAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(ClientContact)
class ClientContactAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(MotionContact)
class MotionContactAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(About)
class AboutAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(Team)
class TeamAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(Person)
class PersonAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(Study)
class StudyAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(CountryPage)
class CountryPageAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(CountryName)
class CountryNamePageAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(ProgramType)
class ProgramTypeAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(Speciality)
class SpecialityAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(Language)
class LanguageAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(CountryDescriptionCost)
class CountryDescriptionCostAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(CountryInfo)
class CountryInfoAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(University)
class UniversityAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(UniversityInfo)
class UniversityInfoAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(UniversityEvent)
class UniversityEventAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(UniversityEventInfo)
class UniversityEventInfoAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(UniversityCost)
class UniversityCostAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(Share)
class ShareAdmin(TranslationAdmin, GeneralMedia):
    pass


admin.site.register(HomeContact)
admin.site.register(VideoItem)
admin.site.register(Country)
admin.site.register(CountryPhoto)

admin.site.register(UniversityPhoto)
