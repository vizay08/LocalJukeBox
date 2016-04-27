# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=750)),
                ('author', models.CharField(max_length=750)),
                ('counter', models.IntegerField()),
                ('coverimage_location', models.IntegerField(max_length=1000)),
                ('is_playing', models.BooleanField()),
            ],
        ),
    ]