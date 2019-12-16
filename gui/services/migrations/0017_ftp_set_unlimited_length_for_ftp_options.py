# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-30 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0016_dyndns_switch_to_inadyn_troglobit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ftp',
            name='ftp_options',
            field=models.TextField(blank=True, help_text='These parameters are added to proftpd.conf.', verbose_name='Auxiliary parameters'),
        ),
    ]