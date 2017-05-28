# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import data.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuiltBy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=data.models.built_image, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Repositories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=16, null=True, blank=True)),
                ('description', models.TextField()),
                ('rating', models.IntegerField()),
                ('connections', models.IntegerField()),
                ('language', models.CharField(max_length=16, null=True, blank=True)),
                ('built_by', models.ManyToManyField(to='data.BuiltBy', blank=True)),
            ],
        ),
    ]
