# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 09:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20160926_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Property')),
            ],
        ),
        migrations.CreateModel(
            name='Lease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Floor')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Property')),
            ],
        ),
        migrations.AddField(
            model_name='availability',
            name='floor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Floor'),
        ),
        migrations.AddField(
            model_name='availability',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Property'),
        ),
        migrations.AddField(
            model_name='property',
            name='country',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='data.Country'),
        ),
    ]