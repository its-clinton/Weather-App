# Generated by Django 4.2.1 on 2023-06-03 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_city_zipcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='ZipCode',
        ),
    ]