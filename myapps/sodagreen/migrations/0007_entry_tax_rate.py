# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sodagreen', '0006_entry_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='tax_rate',
            field=models.FloatField(default=1.08),
        ),
    ]
