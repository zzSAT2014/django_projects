# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sodagreen', '0009_auto_20150819_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='budget',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
