# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-20 13:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addresses_viewer', '0002_address_place_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='place_id',
        ),
        migrations.AlterUniqueTogether(
            name='address',
            unique_together=set([('lat', 'lng')]),
        ),
    ]
