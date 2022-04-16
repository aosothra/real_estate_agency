# Generated by Django 2.2.24 on 2022-04-13 17:07

from django.apps.registry import Apps
from django.db import migrations


def transfer_owner_from_flat(apps: Apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all().iterator():
        owner, _ = Owner.objects.get_or_create(
            fullname=flat.owner,
            phone=flat.owners_phonenumber,
            pure_phone=flat.owners_pure_phone
        )
        owner.flats.add(flat)
        owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_owner'),
    ]

    operations = [
        migrations.RunPython(transfer_owner_from_flat)
    ]
