# Generated by Django 2.2.24 on 2022-04-13 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20220413_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='is_building_new',
            field=models.BooleanField(db_index=True, verbose_name='Новостройка'),
        ),
    ]