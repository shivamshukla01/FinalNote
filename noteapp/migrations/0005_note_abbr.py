# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-18 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0004_auto_20170518_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='abbr',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
