# Generated by Django 2.2.13 on 2020-07-02 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_affiliation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.TextField(blank=True, help_text='The role of the user.', null=True, verbose_name='Role of User'),
        ),
    ]
