# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coltrane', '0003_auto_20150729_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='categories',
            field=models.ManyToManyField(to='coltrane.Category'),
        ),
    ]
