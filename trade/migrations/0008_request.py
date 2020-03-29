# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-11-23 05:20
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0007_merge_20181122_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('requestID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('commodityName', models.CharField(max_length=50)),
                ('exporterName', models.CharField(max_length=50)),
                ('quantityRequested', models.IntegerField()),
            ],
        ),
    ]