# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sodagreen', '0012_auto_20150819_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='title',
            field=models.CharField(default=b'test', help_text=b'maxlength: 250 chars', max_length=250),
        ),
    ]
