# Generated by Django 3.2.11 on 2022-06-13 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0106_auto_20220609_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='computational_thinking_links_de',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='computational_thinking_links_en',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='computational_thinking_links_es',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='computational_thinking_links_fr',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='computational_thinking_links_mi',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='computational_thinking_links_xx_lr',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='computational_thinking_links_yy_rl',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='computational_thinking_links_zh_hans',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='whats_it_all_about_de',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='whats_it_all_about_en',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='whats_it_all_about_es',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='whats_it_all_about_fr',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='whats_it_all_about_heading_tree_de',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='whats_it_all_about_heading_tree_en',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='whats_it_all_about_heading_tree_es',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='whats_it_all_about_heading_tree_fr',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='whats_it_all_about_heading_tree_mi',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='whats_it_all_about_heading_tree_xx_lr',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='whats_it_all_about_heading_tree_yy_rl',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='whats_it_all_about_heading_tree_zh_hans',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='whats_it_all_about_mi',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='whats_it_all_about_xx_lr',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='whats_it_all_about_yy_rl',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='whats_it_all_about_zh_hans',
            field=models.TextField(default='', null=True),
        ),
    ]