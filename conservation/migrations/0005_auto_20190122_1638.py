# Generated by Django 2.0.8 on 2019-01-22 08:38

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0016_auto_20190122_1638'),
        ('conservation', '0004_auto_20190122_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManagementAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_area', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, help_text='If this action pertains to only some but not all occurrences, indicate the target area(s) here. This management action will be automatically affiliated with all intersecting occurrence areas.', null=True, srid=4326, verbose_name='Target Area')),
                ('occurrence_area_code', models.CharField(blank=True, help_text='The known code for the occurrence area this management action pertains to, either a Fauna site, a Flora (sub)population ID, or a TEC/PEC boundary name.', max_length=1000, null=True, verbose_name='Occurence area code')),
                ('instructions', models.TextField(blank=True, help_text='Details on the intended implementation.', null=True, verbose_name='Instructions')),
                ('category', models.ForeignKey(blank=True, help_text='Choose the overarching category.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='conservation.ManagementActionCategory', verbose_name='Managment action category')),
                ('communities', models.ManyToManyField(blank=True, help_text='All communities this management action pertains to.', to='taxonomy.Community', verbose_name='Communities')),
                ('taxa', models.ManyToManyField(blank=True, help_text='All taxa this management action pertains to.', to='taxonomy.Taxon', verbose_name='Taxa')),
            ],
            options={
                'verbose_name': 'Management Action',
                'verbose_name_plural': 'Management Actions',
            },
        ),
        migrations.AddField(
            model_name='document',
            name='management_actions',
            field=models.ManyToManyField(blank=True, help_text='Management actions to be undertaken on all occurences of the subject as specified in the document.', related_name='management_actions_per_document', to='conservation.ManagementAction', verbose_name='Management Action'),
        ),
    ]
