# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sodagreen', '0014_entry_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='slug',
            field=models.SlugField(default=b'', unique_for_date=b'pub_date'),
        ),
    ]
