# Generated by Django 4.2.5 on 2023-10-27 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_remove_ride_passageiros_aceitaram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='available_seats',
            field=models.PositiveIntegerField(default=0),
        ),
    ]