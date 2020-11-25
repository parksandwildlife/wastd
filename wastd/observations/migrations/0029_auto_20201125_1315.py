# Generated by Django 3.0.8 on 2020-11-25 05:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0028_auto_20200811_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoggerObservation',
            fields=[
                ('observation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='observations.Observation')),
                ('logger_type', models.CharField(choices=[('temperature-logger', 'Temperature Logger'), ('data-logger', 'Data Logger'), ('ctd-data-logger', 'Conductivity, Temperature, Depth SR data logger')], default='temperature-logger', help_text='The logger type.', max_length=300, verbose_name='Type')),
                ('deployment_status', models.CharField(choices=[('programmed', 'programmed'), ('posted', 'posted to field team'), ('deployed', 'deployed in situ'), ('resighted', 'resighted in situ'), ('retrieved', 'retrieved in situ'), ('downloaded', 'downloaded')], default='resighted', help_text='The logger life cycle status.', max_length=300, verbose_name='Status')),
                ('logger_id', models.CharField(blank=True, help_text='The ID of a logger must be unique within the tag type.', max_length=1000, null=True, verbose_name='Logger ID')),
            ],
            options={
                'verbose_name': 'Logger Observation',
            },
            bases=('observations.observation',),
        ),
        migrations.AlterModelOptions(
            name='dispatchrecord',
            options={'verbose_name': 'Dispatch Record'},
        ),
        migrations.AlterModelOptions(
            name='dugongmorphometricobservation',
            options={'verbose_name': 'Dugong Morphometric Observation'},
        ),
        migrations.AlterModelOptions(
            name='hatchlingmorphometricobservation',
            options={'verbose_name': 'Turtle Hatchling Morphometric Observation'},
        ),
        migrations.AlterModelOptions(
            name='lightsourceobservation',
            options={'verbose_name': 'Turtle Hatchling Light Source Observation (Fan Angle)', 'verbose_name_plural': 'Turtle Hatchling Light Source Observations (Fan Angles)'},
        ),
        migrations.AlterModelOptions(
            name='managementaction',
            options={'verbose_name': 'Management Action'},
        ),
        migrations.AlterModelOptions(
            name='mediaattachment',
            options={'verbose_name': 'Media Attachment'},
        ),
        migrations.AlterModelOptions(
            name='nesttagobservation',
            options={'verbose_name': 'Turtle Nest Tag Observation'},
        ),
        migrations.AlterModelOptions(
            name='tagobservation',
            options={'verbose_name': 'Turtle Tag Observation'},
        ),
        migrations.AlterModelOptions(
            name='temperatureloggerdeployment',
            options={'verbose_name': 'Temperature Logger Deployment'},
        ),
        migrations.AlterModelOptions(
            name='temperatureloggersettings',
            options={'verbose_name': 'Temperature Logger Setting'},
        ),
        migrations.AlterModelOptions(
            name='tracktallyobservation',
            options={'verbose_name': 'Turtle Track Tally Observation'},
        ),
        migrations.AlterModelOptions(
            name='turtledamageobservation',
            options={'verbose_name': 'Turtle Damage Observation'},
        ),
        migrations.AlterModelOptions(
            name='turtlehatchlingemergenceobservation',
            options={'verbose_name': 'Turtle Hatchling Emergence Observation (Fan Angle)', 'verbose_name_plural': 'Turtle Hatchling Emergence Observations (Fan Angles)'},
        ),
        migrations.AlterModelOptions(
            name='turtlehatchlingemergenceoutlierobservation',
            options={'verbose_name': 'Turtle Hatchling Emergence Outlier Observation (Fan Angle)', 'verbose_name_plural': 'Turtle Hatchling Emergence Outlier Observations (Fan Angles)'},
        ),
        migrations.AlterModelOptions(
            name='turtlemorphometricobservation',
            options={'verbose_name': 'Turtle Morphometric Observation'},
        ),
        migrations.AlterModelOptions(
            name='turtlenestdisturbanceobservation',
            options={'verbose_name': 'Turtle Nest Disturbance Observation'},
        ),
        migrations.AlterModelOptions(
            name='turtlenestdisturbancetallyobservation',
            options={'verbose_name': 'Turtle Nest Disturbance Tally Observation'},
        ),
        migrations.AlterModelOptions(
            name='turtlenestobservation',
            options={'verbose_name': 'Turtle Nest Excavation (Egg count)', 'verbose_name_plural': 'Turtle Nest Excavations (Egg count)'},
        ),
        migrations.AddField(
            model_name='turtlemorphometricobservation',
            name='curved_carapace_length_min_accuracy',
            field=models.CharField(blank=True, choices=[('1', 'To nearest 1 mm'), ('5', 'To nearest 5 mm'), ('10', 'To nearest 1 cm'), ('100', 'To nearest 10 cm'), ('1000', 'To nearest 1 m or 1 kg'), ('5000', 'To nearest 5 m or 5 kg'), ('10000', 'To nearest 10 m or 10 kg')], help_text='The expected measurement accuracy.', max_length=300, null=True, verbose_name='Curved carapace length accuracy'),
        ),
        migrations.AddField(
            model_name='turtlemorphometricobservation',
            name='curved_carapace_length_min_mm',
            field=models.PositiveIntegerField(blank=True, help_text='The curved carapace length (min) in millimetres.', null=True, verbose_name='Curved carapace length min (mm)'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='source_id',
            field=models.CharField(default=uuid.UUID('3551969e-2edd-11eb-a2a6-7107864c7884'), help_text='The ID of the record in the original source, if available.', max_length=1000, verbose_name='Source ID'),
        ),
        migrations.AlterField(
            model_name='tagobservation',
            name='status',
            field=models.CharField(choices=[('ordered', 'ordered from manufacturer'), ('produced', 'produced by manufacturer'), ('delivered', 'delivered to HQ'), ('allocated', 'allocated to field team'), ('applied-new', 'applied new'), ('resighted', 're-sighted associated with animal'), ('reclinched', 're-sighted and reclinched on animal'), ('removed', 'taken off animal'), ('found', 'found detached'), ('returned', 'returned to HQ'), ('decommissioned', 'decommissioned'), ('destroyed', 'destroyed'), ('observed', 'observed in any other context, see comments')], default='resighted', help_text='The status this tag was after the encounter.', max_length=300, verbose_name='Tag status'),
        ),
        migrations.AlterField(
            model_name='tagobservation',
            name='tag_type',
            field=models.CharField(choices=[('flipper-tag', 'Flipper Tag'), ('tag-scar', 'Tag Scar'), ('pit-tag', 'PIT Tag'), ('sat-tag', 'Satellite Relay Data Logger'), ('blood-sample', 'Blood Sample'), ('biopsy-sample', 'Biopsy Sample'), ('stomach-content-sample', 'Stomach Content Sample'), ('physical-sample', 'Physical Sample'), ('egg-sample', 'Egg Sample'), ('qld-monel-a-flipper-tag', 'QLD Monel Series A flipper tag'), ('qld-titanium-k-flipper-tag', 'QLD Titanium Series K flipper tag'), ('qld-titanium-t-flipper-tag', 'QLD Titanium Series T flipper tag'), ('acoustic-tag', 'Acoustic tag'), ('commonwealth-titanium-flipper-tag', 'Commonwealth titanium flipper tag (old db value)'), ('cmlth-titanium-flipper-tag', 'Commonwealth titanium flipper tag'), ('cayman-juvenile-tag', 'Cayman juvenile tag'), ('hawaii-inconel-flipper-tag', 'Hawaii Inst Mar Biol Inconel tag'), ('ptt', 'Platform Transmitter Terminal (PTT)'), ('rototag', 'RotoTag'), ('narangebub-nickname', 'Narangebup rehab informal name'), ('aqwa-nickname', 'AQWA informal name'), ('atlantis-nickname', 'Atlantis informal name'), ('wa-museum-reptile-registration-number', 'WA Museum Natural History Reptiles Catalogue Registration Number (old db value)'), ('wam-reptile-registration-number', 'WA Museum Natural History Reptiles Catalogue Registration Number'), ('genetic-tag', 'Genetic ID sequence'), ('other', 'Other')], default='flipper-tag', help_text='What kind of tag is it?', max_length=300, verbose_name='Tag type'),
        ),
        migrations.AlterField(
            model_name='turtlehatchlingemergenceobservation',
            name='light_sources_present',
            field=models.CharField(choices=[('na', 'NA'), ('absent', 'Confirmed absent'), ('present', 'Confirmed present')], default='na', help_text='', max_length=300, verbose_name='Light sources present during emergence'),
        ),
        migrations.AlterField(
            model_name='turtlehatchlingemergenceobservation',
            name='outlier_tracks_present',
            field=models.CharField(choices=[('na', 'NA'), ('absent', 'Confirmed absent'), ('present', 'Confirmed present')], default='na', help_text='', max_length=300, verbose_name='Outlier tracks present'),
        ),
        migrations.AlterField(
            model_name='turtlehatchlingemergenceoutlierobservation',
            name='outlier_group_size',
            field=models.PositiveIntegerField(blank=True, help_text='', null=True, verbose_name='Number of tracks in outlier group'),
        ),
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='body_depth_accuracy',
            field=models.CharField(blank=True, choices=[('1', 'To nearest 1 mm'), ('5', 'To nearest 5 mm'), ('10', 'To nearest 1 cm'), ('100', 'To nearest 10 cm'), ('1000', 'To nearest 1 m or 1 kg'), ('5000', 'To nearest 5 m or 5 kg'), ('10000', 'To nearest 10 m or 10 kg')], help_text='The expected measurement accuracy.', max_length=300, null=True, verbose_name='Body depth accuracy'),
        ),
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='body_weight_accuracy',
            field=models.CharField(blank=True, choices=[('1', 'To nearest 1 mm'), ('5', 'To nearest 5 mm'), ('10', 'To nearest 1 cm'), ('100', 'To nearest 10 cm'), ('1000', 'To nearest 1 m or 1 kg'), ('5000', 'To nearest 5 m or 5 kg'), ('10000', 'To nearest 10 m or 10 kg')], help_text='The expected measurement accuracy.', max_length=300, null=True, verbose_name='Body weight accuracy'),
        ),
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='curved_carapace_length_accuracy',
            field=models.CharField(blank=True, choices=[('1', 'To nearest 1 mm'), ('5', 'To nearest 5 mm'), ('10', 'To nearest 1 cm'), ('100', 'To nearest 10 cm'), ('1000', 'To nearest 1 m or 1 kg'), ('5000', 'To nearest 5 m or 5 kg'), ('10000', 'To nearest 10 m or 10 kg')], help_text='The expected measurement accuracy.', max_length=300, null=True, verbose_name='Curved carapace length (max) accuracy'),
        ),
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='curved_carapace_length_mm',
            field=models.PositiveIntegerField(blank=True, help_text='The curved carapace length (max) in millimetres.', null=True, verbose_name='Curved carapace length max (mm)'),
        ),
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='curved_carapace_width_accuracy',
            field=models.CharField(blank=True, choices=[('1', 'To nearest 1 mm'), ('5', 'To nearest 5 mm'), ('10', 'To nearest 1 cm'), ('100', 'To nearest 10 cm'), ('1000', 'To nearest 1 m or 1 kg'), ('5000', 'To nearest 5 m or 5 kg'), ('10000', 'To nearest 10 m or 10 kg')], help_text='The expected measurement accuracy.', max_length=300, null=True, verbose_name='Curved carapace width (mm)'),
        ),
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='maximum_head_length_accuracy',
            field=models.CharField(blank=True, choices=[('1', 'To nearest 1 mm'), ('5', 'To nearest 5 mm'), ('10', 'To nearest 1 cm'), ('100', 'To nearest 10 cm'), ('1000', 'To nearest 1 m or 1 kg'), ('5000', 'To nearest 5 m or 5 kg'), ('10000', 'To nearest 10 m or 10 kg')], help_text='The expected measurement accuracy.', max_length=300, null=True, verbose_name='Maximum head length accuracy'),
        ),
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='maximum_head_width_accuracy',
            field=models.CharField(blank=True, choices=[('1', 'To nearest 1 mm'), ('5', 'To nearest 5 mm'), ('10', 'To nearest 1 cm'), ('100', 'To nearest 10 cm'), ('1000', 'To nearest 1 m or 1 kg'), ('5000', 'To nearest 5 m or 5 kg'), ('10000', 'To nearest 10 m or 10 kg')], help_text='The expected measurement accuracy.', max_length=300, null=True, verbose_name='Maximum head width accuracy'),
        ),
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='straight_carapace_length_accuracy',
            field=models.CharField(blank=True, choices=[('1', 'To nearest 1 mm'), ('5', 'To nearest 5 mm'), ('10', 'To nearest 1 cm'), ('100', 'To nearest 10 cm'), ('1000', 'To nearest 1 m or 1 kg'), ('5000', 'To nearest 5 m or 5 kg'), ('10000', 'To nearest 10 m or 10 kg')], help_text='The expected measurement accuracy.', max_length=300, null=True, verbose_name='Straight carapace length accuracy'),
        ),
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='tail_length_carapace_accuracy',
            field=models.CharField(blank=True, choices=[('1', 'To nearest 1 mm'), ('5', 'To nearest 5 mm'), ('10', 'To nearest 1 cm'), ('100', 'To nearest 10 cm'), ('1000', 'To nearest 1 m or 1 kg'), ('5000', 'To nearest 5 m or 5 kg'), ('10000', 'To nearest 10 m or 10 kg')], help_text='The expected measurement accuracy.', max_length=300, null=True, verbose_name='Tail length from carapace accuracy'),
        ),
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='tail_length_plastron_accuracy',
            field=models.CharField(blank=True, choices=[('1', 'To nearest 1 mm'), ('5', 'To nearest 5 mm'), ('10', 'To nearest 1 cm'), ('100', 'To nearest 10 cm'), ('1000', 'To nearest 1 m or 1 kg'), ('5000', 'To nearest 5 m or 5 kg'), ('10000', 'To nearest 10 m or 10 kg')], help_text='The expected measurement accuracy.', max_length=300, null=True, verbose_name='Tail length from plastron accuracy'),
        ),
        migrations.AlterField(
            model_name='turtlemorphometricobservation',
            name='tail_length_vent_accuracy',
            field=models.CharField(blank=True, choices=[('1', 'To nearest 1 mm'), ('5', 'To nearest 5 mm'), ('10', 'To nearest 1 cm'), ('100', 'To nearest 10 cm'), ('1000', 'To nearest 1 m or 1 kg'), ('5000', 'To nearest 5 m or 5 kg'), ('10000', 'To nearest 10 m or 10 kg')], help_text='The expected measurement accuracy.', max_length=300, null=True, verbose_name='Tail Length Accuracy'),
        ),
    ]
