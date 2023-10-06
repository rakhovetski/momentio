# Generated by Django 3.2.21 on 2023-10-06 16:20

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='hex_color',
            field=models.CharField(blank=True, default='#4d10bd', max_length=7, null=True, validators=[django.core.validators.RegexValidator(re.compile('^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'), 'Enter a valid color')]),
        ),
    ]