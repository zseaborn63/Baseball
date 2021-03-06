# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lahmanID', models.IntegerField()),
                ('player_key', models.CharField(max_length=10)),
                ('managerID', models.CharField(blank=True, max_length=10)),
                ('hofID', models.CharField(blank=True, max_length=10)),
                ('birthYear', models.IntegerField()),
                ('birthMonth', models.IntegerField()),
                ('birthDay', models.IntegerField()),
                ('birthCountry', models.CharField(max_length=50)),
                ('birthState', models.CharField(blank=True, max_length=2)),
                ('birthCity', models.CharField(max_length=50)),
                ('deathYear', models.IntegerField(blank=True)),
                ('deathMonth', models.IntegerField(blank=True)),
                ('deathDay', models.IntegerField(blank=True)),
                ('deathCountry', models.CharField(blank=True, max_length=50)),
                ('deathState', models.CharField(blank=True, max_length=2)),
                ('deathCity', models.CharField(blank=True, max_length=50)),
                ('nameFirst', models.CharField(max_length=50)),
                ('nameLast', models.CharField(max_length=50)),
                ('nameNote', models.CharField(max_length=255)),
                ('nameGiven', models.CharField(max_length=255)),
                ('nameNick', models.CharField(max_length=255)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('bats', models.CharField(choices=[('L', 'Left'), ('R', 'Right'), ('B', 'Both')], max_length=1)),
                ('throws', models.CharField(choices=[('L', 'Left'), ('R', 'Right'), ('B', 'Both')], max_length=1)),
                ('debut', models.CharField(max_length=12)),
                ('finalGame', models.CharField(blank=True, max_length=12)),
                ('college', models.CharField(blank=True, max_length=50)),
                ('lahman40ID', models.CharField(max_length=9)),
                ('lahman45ID', models.CharField(max_length=9)),
                ('holtzID', models.CharField(max_length=9)),
                ('bbrefID', models.CharField(max_length=9)),
            ],
        ),
    ]
