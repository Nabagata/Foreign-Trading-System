# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-11-27 09:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0014_auto_20181124_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='tradeID',
        ),
    ]
