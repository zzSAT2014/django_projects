# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sodagreen', '0011_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='budget',
            field=models.ForeignKey(default=0, to='sodagreen.Budget'),
        ),
    ]
