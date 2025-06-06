from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin


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


class InfoCardInline(TranslationInlineModelAdmin, admin.TabularInline, GeneralMedia):
    model = InfoCard
    extra = 1


@admin.register(Info)
class InfoAdmin(TranslationAdmin, admin.ModelAdmin, GeneralMedia):
    inlines = [InfoCardInline]


@admin.register(Exam)
class ExamAdmin(TranslationAdmin, GeneralMedia):
    pass


class ExamThemeInline(TranslationInlineModelAdmin, admin.TabularInline, GeneralMedia):
    model = ExamTheme
    extra = 1


@admin.register(ExamCard)
class ExamCardAdmin(TranslationAdmin, admin.ModelAdmin, GeneralMedia):
    inlines = [ExamThemeInline]


class VideoItemInline(admin.TabularInline):
    model = VideoItem
    extra = 1


@admin.register(Video)
class VideoAdmin(TranslationAdmin, GeneralMedia):
    inlines = [VideoItemInline]


@admin.register(ClientContact)
class ClientContactAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(MotionContact)
class MotionContactAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(About)
class AboutAdmin(TranslationAdmin, GeneralMedia):
    pass


class PersonInline(TranslationInlineModelAdmin, admin.TabularInline, GeneralMedia):
    model = Person
    extra = 1


@admin.register(Team)
class TeamAdmin(TranslationAdmin, admin.ModelAdmin, GeneralMedia):
    inlines = [PersonInline]


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


class UniversityPhotoInline(admin.TabularInline):
    model = UniversityPhoto
    extra = 1


@admin.register(University)
class UniversityAdmin(TranslationAdmin, admin.ModelAdmin, GeneralMedia):
    inlines = [UniversityPhotoInline]


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


class CountryPhotoInline(admin.TabularInline):
    model = CountryPhoto
    extra = 1


class CountryAdmin(admin.ModelAdmin):
    inlines = [CountryPhotoInline]


admin.site.register(HomeContact)
admin.site.register(Country, CountryAdmin)
