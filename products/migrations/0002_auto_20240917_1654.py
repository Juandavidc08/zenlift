# Generated by Django 3.2.25 on 2024-09-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='sex',
            field=models.CharField(choices=[('M', 'Men'), ('W', 'Women'), ('U', 'Unisex')], default='U', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=254),
        ),
    ]
