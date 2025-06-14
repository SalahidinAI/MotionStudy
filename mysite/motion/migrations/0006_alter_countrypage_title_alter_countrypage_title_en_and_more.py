# Generated by Django 5.2.2 on 2025-06-07 13:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motion', '0005_universitycost_text_universitycost_text_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrypage',
            name='title',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='countrypage',
            name='title_en',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='countrypage',
            name='title_ky',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='countrypage',
            name='title_ru',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='examcard',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_cards', to='motion.exam'),
        ),
        migrations.AlterField(
            model_name='examtheme',
            name='exam_card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_themes', to='motion.examcard'),
        ),
        migrations.AlterField(
            model_name='infocard',
            name='info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info_cards', to='motion.info'),
        ),
        migrations.AlterField(
            model_name='person',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='motion.team'),
        ),
        migrations.AlterField(
            model_name='videoitem',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students_videos', to='motion.video'),
        ),
    ]
