# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-31 19:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nonprofit', '0004_student_student_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bridgeinstructorenroll',
            name='class_field',
            field=models.ForeignKey(db_column='class_id', on_delete=django.db.models.deletion.CASCADE, to='nonprofit.Class'),
        ),
    ]
