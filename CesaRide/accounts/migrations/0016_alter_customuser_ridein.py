# Generated by Django 4.2.5 on 2023-10-27 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_customuser_ridein'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='ridein',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]
