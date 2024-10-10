# Generated by Django 5.1.1 on 2024-10-10 14:43

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_userprofile_default_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]
