# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0004_auto_20160427_0758'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='token',
            field=models.CharField(default='adad', max_length=6),
        ),
    ]
