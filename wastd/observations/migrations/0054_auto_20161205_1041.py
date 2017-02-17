# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0053_auto_20161116_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='curved_carapace_width_accuracy',
            field=models.CharField(blank=True, choices=[('1', 'To nearest 1 mm'), ('5', 'To nearest 5 mm'), ('10', 'To nearest 1 cm'), ('100', 'To nearest 10 cm'), ('1000', 'To nearest 1 m or 1 kg'), ('10000', 'To nearest 10 m or 10 kg')], help_text='The expected measurement accuracy.', max_length=300, null=True, verbose_name='Curved carapace width c'),
        ),
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='curved_carapace_width_mm',
            field=models.PositiveIntegerField(blank=True, help_text='Curved carapace width in millimetres.', null=True, verbose_name='Curved carapace width (mm)'),
        ),
    ]