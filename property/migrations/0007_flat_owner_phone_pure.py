# Generated by Django 2.2.4 on 2020-08-23 14:47

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_auto_20200823_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owner_phone_pure',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
