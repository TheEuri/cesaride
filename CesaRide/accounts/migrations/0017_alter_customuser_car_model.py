# Generated by Django 4.2.5 on 2023-10-27 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_customuser_ridein'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='car_model',
            field=models.IntegerField(),
        ),
    ]
