# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sodagreen', '0005_auto_20150819_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='tag',
            field=tagging.fields.TagField(max_length=255, blank=True),
        ),
    ]
