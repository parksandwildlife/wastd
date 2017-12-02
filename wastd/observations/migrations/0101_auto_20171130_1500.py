# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 07:00
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import wastd.observations.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('observations', '0100_encounter_survey'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyEnd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(choices=[('direct', 'Direct entry'), ('paper', 'Paper data sheet'), ('odk', 'OpenDataKit mobile data capture'), ('wamtram', 'WAMTRAM 2 tagging DB'), ('ntp-exmouth', 'NTP Access DB Exmouth'), ('ntp-broome', 'NTP Access DB Broome'), ('cet', 'Cetacean strandings DB'), ('pin', 'Pinniped strandings DB')], default='direct', help_text='Where was this record captured initially?', max_length=300, verbose_name='Data Source')),
                ('source_id', models.CharField(blank=True, help_text='The ID of the start point in the original source.', max_length=1000, null=True, verbose_name='Source ID')),
                ('device_id', models.CharField(blank=True, help_text='The ID of the recording device, if available.', max_length=1000, null=True, verbose_name='Device ID')),
                ('end_location', django.contrib.gis.db.models.fields.PointField(blank=True, help_text='The end location as point in WGS84.', null=True, srid=4326, verbose_name='Survey end point')),
                ('end_time', models.DateTimeField(blank=True, help_text="The datetime of leaving the site, shown as local time (no daylight savings), stored as UTC. The time of 'feet in the sand, done recording encounters.'", null=True, verbose_name='Survey end time')),
                ('end_photo', models.FileField(help_text='Site conditions at end of survey.', max_length=500, upload_to=wastd.observations.models.expedition_media, verbose_name='Site photo end')),
                ('end_comments', models.TextField(blank=True, help_text='Describe any circumstances affecting data collection, e.g. days without surveys.', null=True, verbose_name='Comments at finish')),
                ('reporter', models.ForeignKey(blank=True, help_text='The person who captured the start point, ideally this person also recoreded the encounters and end point.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Recorded by')),
            ],
            options={
                'ordering': ['end_location', 'end_time'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='surveyend',
            unique_together=set([('source', 'source_id')]),
        ),
    ]