# Generated by Django 4.2.3 on 2023-07-23 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0007_alter_flight_options_alter_passenger_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flight',
            options={'verbose_name_plural': 'Uçuş Bilgileri'},
        ),
    ]
