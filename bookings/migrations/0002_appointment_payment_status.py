# Generated by Django 5.1.1 on 2024-10-24 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
    ]