# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 04:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0014_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='avilable',
            new_name='available',
        ),
    ]