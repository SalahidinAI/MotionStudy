# Generated by Django 5.2.2 on 2025-06-07 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motion', '0007_rename_flag_country_flag1_country_flag2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='speciality_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='speciality_name_en',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='speciality_name_ky',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='speciality_name_ru',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
