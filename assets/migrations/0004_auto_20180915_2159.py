# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-15 13:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20180915_2141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nic',
            old_name='ip_add',
            new_name='ip_address',
        ),
    ]