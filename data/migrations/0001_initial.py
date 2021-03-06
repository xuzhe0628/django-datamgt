# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=255)),
                ('building_grade', models.CharField(max_length=10)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('description', models.CharField(max_length=1024)),
            ],
        ),
    ]
