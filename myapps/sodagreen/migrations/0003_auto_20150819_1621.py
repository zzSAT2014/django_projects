# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sodagreen', '0002_auto_20150819_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, unique_for_year=b'True'),
        ),
    ]
