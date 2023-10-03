# Generated by Django 4.2.5 on 2023-09-30 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_is_colaborador'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('DR', 'Motorista'), ('PS', 'Passageiro')], default='PS', max_length=2),
        ),
    ]
