# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('coltrane', '0002_entry_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('description_html', models.TextField(blank=True)),
                ('url', models.URLField(unique=True)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('slug', models.SlugField(unique_for_date=b'pub_date')),
                ('tags', tagging.fields.TagField(max_length=255, blank=True)),
                ('enable_comments', models.BooleanField(default=True)),
                ('post_elsewhere', models.BooleanField(default=True, verbose_name=b'Post to Delicious')),
                ('via_name', models.CharField(help_text=b'The name of the person whose site you spotted the link on.', max_length=250, verbose_name=b'Via', blank=True)),
                ('via_url', models.URLField(help_text=b'The URL of the site where you spotted the site', verbose_name=b'Via URL', blank=True)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-pub_date'], 'verbose_name_plural': 'Entries'},
        ),
    ]
