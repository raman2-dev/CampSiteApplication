# Generated by Django 4.2.4 on 2023-08-26 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CampsiteApp', '0003_alter_bookingrecord_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookingrecord',
            options={'managed': True},
        ),
    ]