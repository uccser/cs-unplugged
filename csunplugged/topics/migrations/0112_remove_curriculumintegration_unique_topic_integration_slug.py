# Generated by Django 3.2.16 on 2022-12-05 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0111_curriculumintegration_unique_topic_integration_slug'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='curriculumintegration',
            name='unique_topic_integration_slug',
        ),
    ]
