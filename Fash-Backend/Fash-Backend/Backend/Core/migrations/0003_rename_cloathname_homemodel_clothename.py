# Generated by Django 4.0.4 on 2022-07-26 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_homemodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homemodel',
            old_name='CloathName',
            new_name='ClotheName',
        ),
    ]
