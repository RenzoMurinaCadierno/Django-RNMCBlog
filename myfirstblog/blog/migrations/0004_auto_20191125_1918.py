# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-11-25 22:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191124_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 25, 22, 18, 36, 600331, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 25, 22, 18, 36, 600331, tzinfo=utc)),
        ),
    ]