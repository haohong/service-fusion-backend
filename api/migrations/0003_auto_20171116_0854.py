# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-16 08:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20171116_0424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='birthday',
            new_name='date_of_birth',
        ),
    ]
