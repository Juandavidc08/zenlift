# Generated by Django 5.1.1 on 2024-10-10 14:38

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_country',
            field=django_countries.fields.CountryField(blank=True, default='US', max_length=2),
        ),
    ]
