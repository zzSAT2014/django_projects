# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sodagreen', '0016_entry_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='budget',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AlterField(
            model_name='budget',
            name='amount',
            field=models.FloatField(),
        ),
    ]
