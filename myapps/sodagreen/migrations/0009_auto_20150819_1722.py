# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sodagreen', '0008_auto_20150819_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='category',
        ),
        migrations.AddField(
            model_name='entry',
            name='budget',
            field=models.ForeignKey(default='testing', to='sodagreen.Budget'),
            preserve_default=False,
        ),
    ]
