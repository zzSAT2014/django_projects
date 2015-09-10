# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sodagreen', '0003_auto_20150819_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, unique_for_year=b'category'),
        ),
    ]
