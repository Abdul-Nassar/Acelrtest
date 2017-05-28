# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_builtby_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='builtby',
            name='name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='repositories',
            name='language',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='repositories',
            name='rating',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='repositories',
            name='title',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
