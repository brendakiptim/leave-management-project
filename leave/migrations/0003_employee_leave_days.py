# Generated by Django 3.2.9 on 2022-01-04 10:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0002_auto_20220104_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='leave_days',
            field=models.IntegerField(default=21, validators=[django.core.validators.MaxValueValidator(21), django.core.validators.MinValueValidator(0)]),
        ),
    ]
