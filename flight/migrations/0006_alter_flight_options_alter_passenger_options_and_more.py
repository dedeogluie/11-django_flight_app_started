# Generated by Django 4.2.3 on 2023-07-23 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0005_remove_rezervation_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flight',
            options={'ordering': (('flight_number',),), 'verbose_name_plural': 'Uçuş Bilgileri'},
        ),
        migrations.AlterModelOptions(
            name='passenger',
            options={'ordering': (('firstName',),), 'verbose_name_plural': 'Yolcu Bilgileri'},
        ),
        migrations.AlterModelOptions(
            name='rezervation',
            options={'verbose_name_plural': 'Rezervasyon Bilgileri'},
        ),
    ]
