# Generated by Django 4.0 on 2021-12-14 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dog_owner', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='dog',
            table='dogs',
        ),
        migrations.AlterModelTable(
            name='owner',
            table='owners',
        ),
    ]
