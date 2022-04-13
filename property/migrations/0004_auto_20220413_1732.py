# Generated by Django 2.2.24 on 2022-04-13 13:32

from django.apps.registry import Apps
from django.db import migrations



def flag_new_buildings(apps: Apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.is_building_new = flat.construction_year > 2014
        flat.save()



class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_is_building_new'),
    ]

    operations = [
        migrations.RunPython(flag_new_buildings)
    ]