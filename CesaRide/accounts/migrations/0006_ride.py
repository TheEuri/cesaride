# Generated by Django 4.2.5 on 2023-10-27 02:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_marca_car_brand_rename_modelo_car_model_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_passengers', models.IntegerField()),
                ('time', models.TimeField()),
                ('origin', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('observations', models.TextField(blank=True, null=True)),
                ('passenger_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver', to=settings.AUTH_USER_MODEL)),
                ('passengers', models.ManyToManyField(related_name='passengers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
