# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-09-30 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0019_auto_20160930_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turtlenestobservation',
            name='no_dead_embryos',
        ),
        migrations.RemoveField(
            model_name='turtlenestobservation',
            name='no_dead_full_term_embryos',
        ),
        migrations.AddField(
            model_name='turtlenestobservation',
            name='no_emerged',
            field=models.PositiveIntegerField(blank=True, help_text='The number of hatchlings leaving or departed from nest.', null=True, verbose_name='Emerged (E)'),
        ),
        migrations.AddField(
            model_name='turtlenestobservation',
            name='no_unhatched_eggs',
            field=models.PositiveIntegerField(blank=True, help_text='The number of unhatched eggs with obvious, not yet full term, embryo.', null=True, verbose_name='Unhatched eggs (UH)'),
        ),
        migrations.AddField(
            model_name='turtlenestobservation',
            name='no_unhatched_term',
            field=models.PositiveIntegerField(blank=True, help_text='The number of unhatched, apparently full term, embryo in egg or pipped with small amount of external yolk material.', null=True, verbose_name='Unhatched term (UHT)'),
        ),
        migrations.AlterField(
            model_name='tracktallyobservation',
            name='bird_predation',
            field=models.CharField(choices=[('na', 'NA'), ('absent', 'Confirmed absent'), ('present', 'Confirmed present')], default='na', help_text='', max_length=300, verbose_name='Bird predation'),
        ),
        migrations.AlterField(
            model_name='tracktallyobservation',
            name='croc_predation',
            field=models.CharField(choices=[('na', 'NA'), ('absent', 'Confirmed absent'), ('present', 'Confirmed present')], default='na', help_text='', max_length=300, verbose_name='Crocodile predation'),
        ),
        migrations.AlterField(
            model_name='tracktallyobservation',
            name='dingo_predation',
            field=models.CharField(choices=[('na', 'NA'), ('absent', 'Confirmed absent'), ('present', 'Confirmed present')], default='na', help_text='', max_length=300, verbose_name='Dingo predation'),
        ),
        migrations.AlterField(
            model_name='tracktallyobservation',
            name='dog_predation',
            field=models.CharField(choices=[('na', 'NA'), ('absent', 'Confirmed absent'), ('present', 'Confirmed present')], default='na', help_text='', max_length=300, verbose_name='Dog predation'),
        ),
        migrations.AlterField(
            model_name='tracktallyobservation',
            name='fox_predation',
            field=models.CharField(choices=[('na', 'NA'), ('absent', 'Confirmed absent'), ('present', 'Confirmed present')], default='na', help_text='', max_length=300, verbose_name='Fox predation'),
        ),
        migrations.AlterField(
            model_name='tracktallyobservation',
            name='goanna_predation',
            field=models.CharField(choices=[('na', 'NA'), ('absent', 'Confirmed absent'), ('present', 'Confirmed present')], default='na', help_text='', max_length=300, verbose_name='Goanna predation'),
        ),
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='body_depth_accuracy',
            field=models.CharField(blank=True, choices=[('1', 'To nearest 1 mm'), ('10', 'To nearest 1 cm'), ('100', 'To nearest 10 cm'), ('1000', 'To nearest 1 m or 1 kg'), ('10000', 'To nearest 10 m or 10 kg')], help_text='The expected measurement accuracy.', max_length=300, null=True, verbose_name='Body depth accuracy'),
        ),
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='body_weight_accuracy',
            field=models.CharField(blank=True, choices=[('1', 'To nearest 1 mm'), ('10', 'To nearest 1 cm'), ('100', 'To nearest 10 cm'), ('1000', 'To nearest 1 m or 1 kg'), ('10000', 'To nearest 10 m or 10 kg')], help_text='The expected measurement accuracy.', max_length=300, null=True, verbose_name='Body weight accuracy'),
        ),
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='curved_carapace_length_accuracy',
            field=models.CharField(blank=True, choices=[('1', 'To nearest 1 mm'), ('10', 'To nearest 1 cm'), ('100', 'To nearest 10 cm'), ('1000', 'To nearest 1 m or 1 kg'), ('10000', 'To nearest 10 m or 10 kg')], help_text='The expected measurement accuracy.', max_length=300, null=True, verbose_name='Curved carapace length accuracy'),
        ),
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='curved_carapace_width_accuracy',
            field=models.CharField(blank=True, choices=[('1', 'To nearest 1 mm'), ('10', 'To nearest 1 cm'), ('100', 'To nearest 10 cm'), ('1000', 'To nearest 1 m or 1 kg'), ('10000', 'To nearest 10 m or 10 kg')], help_text='The expected measurement accuracy.', max_length=300, null=True, verbose_name='Curved carapace width accuracy'),
        ),
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='maximum_head_length_accuracy',
            field=models.CharField(blank=True, choices=[('1', 'To nearest 1 mm'), ('10', 'To nearest 1 cm'), ('100', 'To nearest 10 cm'), ('1000', 'To nearest 1 m or 1 kg'), ('10000', 'To nearest 10 m or 10 kg')], help_text='The expected measurement accuracy.', max_length=300, null=True, verbose_name='Maximum head length accuracy'),
        ),
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='maximum_head_width_accuracy',
            field=models.CharField(blank=True, choices=[('1', 'To nearest 1 mm'), ('10', 'To nearest 1 cm'), ('100', 'To nearest 10 cm'), ('1000', 'To nearest 1 m or 1 kg'), ('10000', 'To nearest 10 m or 10 kg')], help_text='The expected measurement accuracy.', max_length=300, null=True, verbose_name='Maximum head width accuracy'),
        ),
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='straight_carapace_length_accuracy',
            field=models.CharField(blank=True, choices=[('1', 'To nearest 1 mm'), ('10', 'To nearest 1 cm'), ('100', 'To nearest 10 cm'), ('1000', 'To nearest 1 m or 1 kg'), ('10000', 'To nearest 10 m or 10 kg')], help_text='The expected measurement accuracy.', max_length=300, null=True, verbose_name='Straight carapace length accuracy'),
        ),
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='tail_length_carapace_accuracy',
            field=models.CharField(blank=True, choices=[('1', 'To nearest 1 mm'), ('10', 'To nearest 1 cm'), ('100', 'To nearest 10 cm'), ('1000', 'To nearest 1 m or 1 kg'), ('10000', 'To nearest 10 m or 10 kg')], help_text='The expected measurement accuracy.', max_length=300, null=True, verbose_name='Tail length from carapace accuracy'),
        ),
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='tail_length_plastron_accuracy',
            field=models.CharField(blank=True, choices=[('1', 'To nearest 1 mm'), ('10', 'To nearest 1 cm'), ('100', 'To nearest 10 cm'), ('1000', 'To nearest 1 m or 1 kg'), ('10000', 'To nearest 10 m or 10 kg')], help_text='The expected measurement accuracy.', max_length=300, null=True, verbose_name='Tail length from plastron accuracy'),
        ),
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='tail_length_vent_accuracy',
            field=models.CharField(blank=True, choices=[('1', 'To nearest 1 mm'), ('10', 'To nearest 1 cm'), ('100', 'To nearest 10 cm'), ('1000', 'To nearest 1 m or 1 kg'), ('10000', 'To nearest 10 m or 10 kg')], help_text='The expected measurement accuracy.', max_length=300, null=True, verbose_name='Tail Length Accuracy'),
        ),
        migrations.AlterField(
            model_name='turtlenestobservation',
            name='no_dead_hatchlings',
            field=models.PositiveIntegerField(blank=True, help_text='The number of dead hatchlings that have left their shells.', null=True, verbose_name='Dead hatchlings (D)'),
        ),
        migrations.AlterField(
            model_name='turtlenestobservation',
            name='no_depredated_eggs',
            field=models.PositiveIntegerField(blank=True, help_text='The number of open, nearly complete shells containing egg residue.', null=True, verbose_name='Depredated eggs (P)'),
        ),
        migrations.AlterField(
            model_name='turtlenestobservation',
            name='no_egg_shells',
            field=models.PositiveIntegerField(blank=True, help_text='The number of empty shells counted which were more than 50 percent complete.', null=True, verbose_name='Egg shells (S)'),
        ),
        migrations.AlterField(
            model_name='turtlenestobservation',
            name='no_live_hatchlings',
            field=models.PositiveIntegerField(blank=True, help_text='The number of live hatchlings left among shells excluding those in neck of nest.', null=True, verbose_name='Live hatchlings (L)'),
        ),
        migrations.AlterField(
            model_name='turtlenestobservation',
            name='no_undeveloped_eggs',
            field=models.PositiveIntegerField(blank=True, help_text='The number of unhatched eggs with no obvious embryo.', null=True, verbose_name='Undeveloped eggs (UD)'),
        ),
    ]
