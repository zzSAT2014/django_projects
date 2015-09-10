# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sodagreen', '0007_entry_tax_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='detail',
            field=models.TextField(blank=True),
        ),
    ]
