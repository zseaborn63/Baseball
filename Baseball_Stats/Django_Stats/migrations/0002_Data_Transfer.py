# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 16:14
from __future__ import unicode_literals

from django.db import migrations, models
from play import load_player_data


class Migration(migrations.Migration):

    dependencies = [
        ('Django_Stats', '0001_Initial'),
    ]

    operations = [

        migrations.RunPython(load_player_data),
        
    ]
