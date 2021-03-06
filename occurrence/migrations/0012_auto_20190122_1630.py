# Generated by Django 2.0.8 on 2019-01-22 08:30

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occurrence', '0011_auto_20190118_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areaencounter',
            name='source_id',
            field=models.CharField(default=uuid.UUID('f92ac4b2-1e1f-11e9-a86f-ecf4bb19b5fc'), help_text='The ID of the record in the original source, if available.', max_length=1000, verbose_name='Source ID'),
        ),
    ]
