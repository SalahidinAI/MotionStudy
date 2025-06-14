# Generated by Django 5.2.2 on 2025-06-08 08:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motion', '0008_alter_speciality_speciality_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='photo',
            field=models.ImageField(default=1, upload_to='university_photo/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='country',
            name='country_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='countries', to='motion.countrypage'),
        ),
        migrations.AlterField(
            model_name='country',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='countries', to='motion.countryname'),
        ),
        migrations.AlterField(
            model_name='countrydescriptioncost',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_descriptions', to='motion.country'),
        ),
        migrations.AlterField(
            model_name='countryinfo',
            name='country_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_info', to='motion.country'),
        ),
        migrations.AlterField(
            model_name='countryphoto',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_photos', to='motion.country'),
        ),
    ]
