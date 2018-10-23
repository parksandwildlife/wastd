# Generated by Django 2.0.8 on 2018-10-22 04:15

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0004_auto_20181022_1215'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('occurrence', '0002_auto_20180926_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaEncounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('encountered_on', models.DateTimeField(blank=True, help_text='The datetime of the original encounter.', null=True, verbose_name='Encountered on')),
                ('source', models.PositiveIntegerField(choices=[(0, 'Direct entry'), (1, 'Manual entry from paper datasheet'), (2, 'Digital data capture (ODK)'), (10, 'Threatened Fauna'), (11, 'Threatened Flora'), (12, 'Threatened Communities'), (20, 'Turtle Tagging Database WAMTRAM2'), (21, 'Ningaloo Turtle Program'), (22, 'Broome  Turtle Program'), (23, 'Pt Hedland Turtle Program'), (24, 'Gnaraloo Turtle Program'), (25, 'Eco Beach Turtle Program'), (30, 'Cetacean Strandings Database'), (31, 'Pinniped Strandings Database')], default=0, help_text='Where was this record captured initially?', verbose_name='Data Source')),
                ('source_id', models.CharField(blank=True, help_text='The ID of the record in the original source, if available.', max_length=1000, null=True, verbose_name='Source ID')),
                ('status', django_fsm.FSMField(choices=[('new', 'New'), ('proofread', 'Proofread'), ('curated', 'Curated'), ('published', 'Published')], default='new', max_length=50, verbose_name='QA Status')),
                ('code', models.CharField(help_text='A URL-safe, short code. Multiple records of the same Area will be recognised by the same area type and code.', max_length=1000, verbose_name='Code')),
                ('label', models.CharField(blank=True, editable=False, help_text="A short but comprehensive label, populated from the model's string representation.", max_length=1000, null=True, verbose_name='Label')),
                ('name', models.CharField(blank=True, help_text='A human-readable name.', max_length=1000, null=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, help_text='A comprehensive description.', null=True, verbose_name='Description')),
                ('area_type', models.PositiveIntegerField(choices=[(0, 'Ephemeral Site'), (1, 'Permanent Site'), (2, 'Critical Habitat'), (10, 'TEC Boundary'), (11, 'TEC Buffer'), (12, 'TEC Site'), (20, 'Flora Population'), (21, 'Flora Subpopulation'), (30, 'Fauna Site'), (40, 'Marine Protected Area'), (41, 'Locality')], default=0, help_text='The area type.', verbose_name='Area type')),
                ('accuracy', models.FloatField(blank=True, help_text='The measured or estimated accuracy of the location in meters.', null=True, verbose_name='Accuracy [m]')),
                ('point', django.contrib.gis.db.models.fields.PointField(blank=True, help_text="A Point representing the Area. If empty, the centroid will be calculated from the Area's polygon extent.", null=True, srid=4326, verbose_name='Representative Point')),
                ('northern_extent', models.FloatField(blank=True, editable=False, help_text='The northernmost latitude serves to sort areas.', null=True, verbose_name='Northernmost latitude')),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(blank=True, help_text='The exact extent of the area as polygon in WGS84, if available.', null=True, srid=4326, verbose_name='Location')),
                ('as_html', models.TextField(blank=True, editable=False, help_text='The cached HTML representation for display purposes.', null=True, verbose_name='HTML representation')),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
                'ordering': ['-northern_extent', 'name'],
            },
        ),
        migrations.RemoveField(
            model_name='area',
            name='encountered_by',
        ),
        migrations.RemoveField(
            model_name='area',
            name='polymorphic_ctype',
        ),
        migrations.RemoveField(
            model_name='communityarea',
            name='area_ptr',
        ),
        migrations.RemoveField(
            model_name='communityarea',
            name='community',
        ),
        migrations.RemoveField(
            model_name='taxonarea',
            name='area_ptr',
        ),
        migrations.RemoveField(
            model_name='taxonarea',
            name='taxon',
        ),
        migrations.CreateModel(
            name='CommunityAreaEncounter',
            fields=[
                ('areaencounter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='occurrence.AreaEncounter')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_related_areas', to='taxonomy.Community')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('occurrence.areaencounter',),
        ),
        migrations.CreateModel(
            name='TaxonAreaEncounter',
            fields=[
                ('areaencounter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='occurrence.AreaEncounter')),
                ('taxon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taxon_related_areas', to='taxonomy.Taxon')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('occurrence.areaencounter',),
        ),
        migrations.DeleteModel(
            name='Area',
        ),
        migrations.DeleteModel(
            name='CommunityArea',
        ),
        migrations.DeleteModel(
            name='TaxonArea',
        ),
        migrations.AddField(
            model_name='areaencounter',
            name='encountered_by',
            field=models.ForeignKey(blank=True, help_text='The person who experience the original encounter.', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Encountered by'),
        ),
        migrations.AddField(
            model_name='areaencounter',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_occurrence.areaencounter_set+', to='contenttypes.ContentType'),
        ),
    ]
