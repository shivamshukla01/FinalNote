# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-18 05:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchname', models.CharField(max_length=100, null=True)),
                ('branch_short', models.CharField(max_length=100, null='TBA')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('abbrev', models.CharField(default='TBA', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='srcfile',
            field=models.FileField(null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='branch',
            name='included_subjects',
            field=models.ManyToManyField(to='noteapp.Subject'),
        ),
        migrations.AddField(
            model_name='note',
            name='subj',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='noteapp.Subject'),
        ),
    ]
