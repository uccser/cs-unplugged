# Generated by Django 3.2.15 on 2022-08-21 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('at_a_distance', '0006_alter_lesson_order_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='introduction_xx_lr',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='introduction_yy_rl',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='name_xx_lr',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='name_yy_rl',
        ),
    ]