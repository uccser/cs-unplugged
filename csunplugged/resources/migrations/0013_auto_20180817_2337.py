# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-17 23:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0012_auto_20180727_0031'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resource',
            options={'ordering': ['name']},
        ),
    ]
