# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-08 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangaki', '0078_auto_20170706_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='anidb_tag_id',
            field=models.IntegerField(unique=True)
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
