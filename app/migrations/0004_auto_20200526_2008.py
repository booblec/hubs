# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-26 17:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200526_1851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='autor',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 26, 20, 7, 51, 893034), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 26, 20, 7, 51, 894035), verbose_name='Дата'),
        ),
    ]
