# Generated by Django 5.1.1 on 2024-10-14 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='bio',
            field=models.TextField(max_length=250),
        ),
    ]
