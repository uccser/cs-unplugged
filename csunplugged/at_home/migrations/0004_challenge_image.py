# Generated by Django 2.2.12 on 2020-05-29 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('at_home', '0003_auto_20200513_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='image',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]