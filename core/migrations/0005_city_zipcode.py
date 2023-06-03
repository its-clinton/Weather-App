# Generated by Django 4.2.1 on 2023-06-03 13:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_city_delete_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='ZipCode',
            field=models.CharField(default=django.utils.timezone.now, max_length=5),
            preserve_default=False,
        ),
    ]