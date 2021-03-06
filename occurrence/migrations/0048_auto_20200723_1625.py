# Generated by Django 3.0.8 on 2020-07-23 08:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('occurrence', '0047_auto_20200702_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areaencounter',
            name='source_id',
            field=models.CharField(default=uuid.UUID('1626e624-ccbe-11ea-bc01-b70be07a119f'), help_text='The ID of the record in the original source, if available.', max_length=1000, verbose_name='Source ID'),
        ),
    ]
