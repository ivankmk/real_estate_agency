# Generated by Django 2.2.4 on 2020-08-23 17:04

from django.db import migrations
import phonenumbers


def phone_normalizer(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        dirty_phone = flat.owners_phonenumber
        parsed_phone = phonenumbers.parse(dirty_phone, 'RU')
        if phonenumbers.is_valid_number(parsed_phone):
            clean_phone = phonenumbers.format_number(
                parsed_phone,
                phonenumbers.PhoneNumberFormat.E164
            )
            flat.owner_phone_pure = clean_phone
            flat.save()
        else:
            flat.owner_phone_pure = ''
            flat.save()            

def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.owner_phone_pure = ''
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_phone_pure'),
    ]

    operations = [
        migrations.RunPython(phone_normalizer, move_backward)
    ]