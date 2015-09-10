# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sodagreen', '0013_budget_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='title',
            field=models.CharField(default=b'blank', help_text=b'maxlength: 250 chars', max_length=250),
        ),
    ]
