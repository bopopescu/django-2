# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-06 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneplace', '0004_remove_instructor_instructor_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_alt_id',
            field=models.CharField(default='no student id', max_length=50, null=True),
        ),
    ]