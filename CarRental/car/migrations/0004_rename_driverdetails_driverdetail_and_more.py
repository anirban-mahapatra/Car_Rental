# Generated by Django 5.0.3 on 2024-04-01 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_contct_driverdetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DriverDetails',
            new_name='DriverDetail',
        ),
        migrations.RenameModel(
            old_name='UserDetails',
            new_name='UserDetail',
        ),
    ]