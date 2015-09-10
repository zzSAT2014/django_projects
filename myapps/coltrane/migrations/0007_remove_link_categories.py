# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coltrane', '0006_entry_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='categories',
        ),
    ]
