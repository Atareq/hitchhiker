# Generated by Django 2.2.12 on 2023-09-05 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipment',
            old_name='user_shipment',
            new_name='trip_id',
        ),
    ]
