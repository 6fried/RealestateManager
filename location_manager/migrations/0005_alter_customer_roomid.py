# Generated by Django 3.2 on 2021-07-31 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_manager', '0004_auto_20210731_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='roomid',
            field=models.PositiveIntegerField(default=0, unique=True, verbose_name='N° de Chambre'),
        ),
    ]
