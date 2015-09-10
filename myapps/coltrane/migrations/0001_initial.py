# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'MaxChar Allowed: 250', max_length=250)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['title'],
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'MaxChar Allowed: 250', max_length=250)),
                ('excerpt', models.TextField(blank=True)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('slug', models.SlugField(unique_for_date=b'pub_date')),
                ('enable_comments', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=False)),
                ('status', models.IntegerField(default=2, choices=[(1, b'live status'), (2, b'draft status'), (3, b'hidden status')])),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(to='coltrane.Category')),
            ],
            options={
                'verbose_name_plural': 'Entries',
            },
        ),
    ]
