# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coltrane', '0005_remove_entry_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='categories',
            field=models.ManyToManyField(to='coltrane.Category'),
        ),
    ]
