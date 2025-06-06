from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Home(models.Model):
    label = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    description = models.TextField()
    image1 = models.ImageField(upload_to='homehome_images/')
    image2 = models.ImageField(upload_to='homehome_images/')
    image3 = models.ImageField(upload_to='homehome_images/')
    image4 = models.ImageField(upload_to='home_images/')


class HomeContact(models.Model):
    name = models.CharField(max_length=32)
    phone_number = PhoneNumberField()


class Info(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to='info_images/')


class InfoCard(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField()


class Exam(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()


class ExamCard(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='exam_images/')
    image2 = models.ImageField(upload_to='exam_images/')
    exam_type = models.CharField(max_length=64)
    title = models.CharField(max_length=64)


class ExamTheme(models.Model):
    exam_card = models.ForeignKey(ExamCard, on_delete=models.CASCADE)
    theme = models.CharField(max_length=128)
    description = models.TextField()


class Video(models.Model):
    title = models.CharField(max_length=64)


class VideoItem(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    videos = models.FileField(upload_to='student_videos/')


class ClientContact(models.Model):
    title = models.CharField(max_length=32)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    phone = PhoneNumberField()
    email = models.EmailField(unique=True)
    organization = models.CharField(max_length=32)
    text = models.TextField()


class MotionContact(models.Model):
    title = models.CharField(max_length=32)
    phone = PhoneNumberField()
    email = models.EmailField(unique=True)


class About(models.Model):
    image = models.ImageField(upload_to='about_images/')
    label = models.CharField(max_length=16)
    title = models.CharField(max_length=64)
    text = models.TextField()
    description = models.TextField()


class Team(models.Model):
    title = models.CharField(max_length=16)


class Person(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    info = models.CharField(max_length=128)
    profile_image = models.ImageField(upload_to='person_images/')


class Study(models.Model):
    title = models.CharField(max_length=16)
    study_image = models.ImageField(upload_to='study_images/')
    description = models.TextField()
    bonus = models.TextField()


class CountryPage(models.Model):
    title = models.CharField(max_length=16)


class CountryName(models.Model):
    country_name = models.CharField(max_length=32)


class ProgramType(models.Model):
    program = models.CharField(max_length=32)


class Speciality(models.Model):
    speciality_name = models.CharField(max_length=32)


class Language(models.Model):
    language = models.CharField(max_length=32)


class Country(models.Model):
    country_page = models.ForeignKey(CountryPage, on_delete=models.CASCADE)
    flag = models.ImageField(upload_to='country_flags/')
    location = models.ForeignKey(CountryName, on_delete=models.CASCADE)
    program_type = models.ManyToManyField(ProgramType)
    speciality = models.ManyToManyField(Speciality)
    language = models.ManyToManyField(Language)


class CountryDescriptionCost(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    description = models.TextField()


class CountryPhoto(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    country_photos = models.ImageField(upload_to='country_photos/')


# check how to get this page, change the logic if u need
# check the country_name relationship, depends on user_flow
class CountryInfo(models.Model):
    country_name = models.ForeignKey(Country, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    information = models.TextField()


# check the location relationship, depends on user_flow
class University(models.Model):
    title = models.CharField(max_length=64)
    location = models.ForeignKey(Country, on_delete=models.CASCADE)
    foundation_date = models.DateField()
    program_type = models.ManyToManyField(ProgramType)
    speciality = models.ManyToManyField(Speciality)
    language = models.ManyToManyField(Language)


class UniversityInfo(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    information = models.TextField()


class UniversityEvent(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    information = models.TextField()


class UniversityEventInfo(models.Model):
    event = models.ForeignKey(UniversityEvent, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    information = models.TextField()


class UniversityCost(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    text = models.TextField()
    info = models.TextField()


class UniversityPhoto(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    university_photos = models.ImageField(upload_to='university_photos/')


class Share(models.Model):
    title = models.CharField(max_length=16)
    info = models.CharField(max_length=32)
