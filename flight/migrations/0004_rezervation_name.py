# Generated by Django 4.2.3 on 2023-07-20 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0003_alter_flight_date_of_departure_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rezervation',
            name='name',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
