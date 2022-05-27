# Generated by Django 3.2.11 on 2022-05-19 23:11

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0102_auto_20220516_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitplan',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.AddIndex(
            model_name='unitplan',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='topics_unit_search__1551c1_gin'),
        ),
    ]