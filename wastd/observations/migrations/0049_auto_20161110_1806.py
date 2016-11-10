# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0048_auto_20161110_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalencounter',
            name='habitat',
            field=models.CharField(choices=[('na', 'unknown habitat'), ('beach-below-high-water', '(B) beach below high water mark'), ('beach-above-high-water', '(A) beach above high water mark and dune'), ('beach-edge-of-vegetation', '(E) edge of vegetation'), ('in-dune-vegetation', '(V) inside vegetation'), ('beach', 'beach (below vegetation line)'), ('bays-estuaries', 'bays, estuaries and other enclosed shallow soft sediments'), ('dune', 'dune'), ('dune-constructed-hard-substrate', 'dune, constructed hard substrate (concrete slabs, timber floors, helipad)'), ('dune-grass-area', 'dune, grass area'), ('dune-compacted-path', 'dune, hard compacted areas (road ways, paths)'), ('dune-rubble', 'dune, rubble, usually coral'), ('dune-bare-sand', 'dune, bare sand area'), ('dune-beneath-vegetation', 'dune, beneath tree or shrub'), ('slope-front-dune', 'dune, front slope'), ('sand-flats', 'sand flats'), ('slope-grass', 'slope, grass area'), ('slope-bare-sand', 'slope, bare sand area'), ('slope-beneath-vegetation', 'slope, beneath tree or shrub'), ('below-mean-spring-high-water-mark', 'below the mean spring high water line or current level of inundation'), ('lagoon-patch-reef', 'lagoon, patch reef'), ('lagoon-open-sand', 'lagoon, open sand areas'), ('mangroves', 'mangroves'), ('reef-coral', 'coral reef'), ('reef-crest-front-slope', 'reef crest (dries at low water) and front reef slope areas'), ('reef-flat', 'reef flat, dries at low tide'), ('reef-seagrass-flats', 'coral reef with seagrass flats'), ('reef-rocky', 'rocky reef'), ('open-water', 'open water'), ('harbour', 'harbour'), ('boat-ramp', 'boat ramp')], default='na', help_text='The habitat in which the animal was encountered.', max_length=500, verbose_name='Habitat'),
        ),
        migrations.AlterField(
            model_name='temperatureloggerdeployment',
            name='habitat',
            field=models.CharField(choices=[('na', 'unknown habitat'), ('beach-below-high-water', '(B) beach below high water mark'), ('beach-above-high-water', '(A) beach above high water mark and dune'), ('beach-edge-of-vegetation', '(E) edge of vegetation'), ('in-dune-vegetation', '(V) inside vegetation'), ('beach', 'beach (below vegetation line)'), ('bays-estuaries', 'bays, estuaries and other enclosed shallow soft sediments'), ('dune', 'dune'), ('dune-constructed-hard-substrate', 'dune, constructed hard substrate (concrete slabs, timber floors, helipad)'), ('dune-grass-area', 'dune, grass area'), ('dune-compacted-path', 'dune, hard compacted areas (road ways, paths)'), ('dune-rubble', 'dune, rubble, usually coral'), ('dune-bare-sand', 'dune, bare sand area'), ('dune-beneath-vegetation', 'dune, beneath tree or shrub'), ('slope-front-dune', 'dune, front slope'), ('sand-flats', 'sand flats'), ('slope-grass', 'slope, grass area'), ('slope-bare-sand', 'slope, bare sand area'), ('slope-beneath-vegetation', 'slope, beneath tree or shrub'), ('below-mean-spring-high-water-mark', 'below the mean spring high water line or current level of inundation'), ('lagoon-patch-reef', 'lagoon, patch reef'), ('lagoon-open-sand', 'lagoon, open sand areas'), ('mangroves', 'mangroves'), ('reef-coral', 'coral reef'), ('reef-crest-front-slope', 'reef crest (dries at low water) and front reef slope areas'), ('reef-flat', 'reef flat, dries at low tide'), ('reef-seagrass-flats', 'coral reef with seagrass flats'), ('reef-rocky', 'rocky reef'), ('open-water', 'open water'), ('harbour', 'harbour'), ('boat-ramp', 'boat ramp')], default='na', help_text='The habitat in which the nest was encountered.', max_length=500, verbose_name='Habitat'),
        ),
        migrations.AlterField(
            model_name='turtlenestencounter',
            name='habitat',
            field=models.CharField(choices=[('na', 'unknown habitat'), ('beach-below-high-water', '(B) beach below high water mark'), ('beach-above-high-water', '(A) beach above high water mark and dune'), ('beach-edge-of-vegetation', '(E) edge of vegetation'), ('in-dune-vegetation', '(V) inside vegetation')], default='na', help_text='The habitat in which the track or nest was encountered.', max_length=500, verbose_name='Habitat'),
        ),
        migrations.AlterField(
            model_name='turtlenestobservation',
            name='nest_position',
            field=models.CharField(choices=[('na', 'unknown habitat'), ('beach-below-high-water', '(B) beach below high water mark'), ('beach-above-high-water', '(A) beach above high water mark and dune'), ('beach-edge-of-vegetation', '(E) edge of vegetation'), ('in-dune-vegetation', '(V) inside vegetation')], default='unknown', help_text='The position of the nest on the beach.', max_length=300, verbose_name='Beach position'),
        ),
    ]
