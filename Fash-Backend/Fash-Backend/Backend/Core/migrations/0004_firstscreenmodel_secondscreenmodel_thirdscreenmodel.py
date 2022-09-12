# Generated by Django 4.0.4 on 2022-07-26 22:40

import Core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0003_rename_cloathname_homemodel_clothename'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstScreenModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USERID', models.UUIDField()),
                ('Occasion', models.CharField(blank=True, max_length=255, null=True)),
                ('PersonType', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SecondScreenModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USERID', models.UUIDField()),
                ('Occasion', models.CharField(blank=True, max_length=255, null=True)),
                ('PersonType', models.CharField(blank=True, max_length=255, null=True)),
                ('ClotheName', models.CharField(blank=True, max_length=255, null=True)),
                ('Type', models.CharField(blank=True, max_length=255, null=True)),
                ('Color', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ThirdScreenModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USERID', models.UUIDField()),
                ('Occasion', models.CharField(blank=True, max_length=255, null=True)),
                ('PersonType', models.CharField(blank=True, max_length=255, null=True)),
                ('Image', models.ImageField(upload_to=Core.models.upload_to)),
            ],
        ),
    ]