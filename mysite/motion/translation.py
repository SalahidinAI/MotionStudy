from .models import (Home, Info, InfoCard, Exam, ExamCard, ExamTheme, Video,
                     ClientContact, MotionContact, About, Team, Person, Study,
                     CountryPage, CountryName, ProgramType, Speciality, Language,
                     CountryDescriptionCost, CountryInfo, Share, University, UniversityInfo,
                     UniversityEvent, UniversityEventInfo, UniversityCost)
from modeltranslation.translator import TranslationOptions, register


@register(Home)
class HomeTranslationOptions(TranslationOptions):
    fields = ('label', 'title', 'description')


@register(Info)
class InfoTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(InfoCard)
class InfoCardTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(ExamCard)
class ExamCardTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ExamTheme)
class ExamThemeTranslationOptions(TranslationOptions):
    fields = ('theme', 'description')


@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ClientContact)
class ClientContactTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(MotionContact)
class MotionContactTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('label', 'title', 'text', 'description')


@register(Team)
class TeamTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Person)
class PersonTranslationOptions(TranslationOptions):
    fields = ('info',)


@register(Study)
class StudyTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'bonus')


@register(CountryPage)
class CountryPageTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(CountryName)
class CountryNameTranslationOptions(TranslationOptions):
    fields = ('country_name',)


@register(ProgramType)
class ProgramTypeTranslationOptions(TranslationOptions):
    fields = ('program',)


@register(Speciality)
class SpecialityTranslationOptions(TranslationOptions):
    fields = ('speciality_name',)


@register(Language)
class LanguageTranslationOptions(TranslationOptions):
    fields = ('language',)


@register(CountryDescriptionCost)
class CountryDescriptionCostTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(CountryInfo)
class CountryInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'information')


@register(University)
class UniversityTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(UniversityInfo)
class UniversityInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'information')


@register(UniversityEvent)
class UniversityEventTranslationOptions(TranslationOptions):
    fields = ('title', 'information')


@register(UniversityEventInfo)
class UniversityEventInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'information')


@register(UniversityCost)
class UniversityCostTranslationOptions(TranslationOptions):
    fields = ('text', 'info')


@register(Share)
class ShareTranslationOptions(TranslationOptions):
    fields = ('title', 'info')
