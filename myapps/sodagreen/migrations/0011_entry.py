# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sodagreen', '0010_auto_20150819_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField()),
                ('tax_included', models.BooleanField()),
                ('tax_rate', models.FloatField(default=1.08)),
                ('detail', models.TextField(blank=True)),
                ('tag', tagging.fields.TagField(max_length=255, blank=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('budget', models.ForeignKey(to='sodagreen.Budget')),
            ],
        ),
    ]
