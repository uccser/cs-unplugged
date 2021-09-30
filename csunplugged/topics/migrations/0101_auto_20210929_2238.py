# Generated by Django 3.2.7 on 2021-09-29 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0100_auto_20210215_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agegroup',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='classroomresource',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='curriculumarea',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='curriculumintegration',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='glossaryterm',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='learningoutcome',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='heading_tree',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='heading_tree_de',
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='heading_tree_en',
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='heading_tree_es',
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='heading_tree_fr',
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='heading_tree_mi',
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='heading_tree_xx_lr',
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='heading_tree_yy_rl',
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='heading_tree_zh_hans',
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='lessonnumber',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='programmingchallenge',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='programmingchallengedifficulty',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='programmingchallengeimplementation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='programmingchallengelanguage',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='programmingchallengenumber',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='resourcedescription',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='unitplan',
            name='heading_tree',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='unitplan',
            name='heading_tree_de',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='unitplan',
            name='heading_tree_en',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='unitplan',
            name='heading_tree_es',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='unitplan',
            name='heading_tree_fr',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='unitplan',
            name='heading_tree_mi',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='unitplan',
            name='heading_tree_xx_lr',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='unitplan',
            name='heading_tree_yy_rl',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='unitplan',
            name='heading_tree_zh_hans',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='unitplan',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
