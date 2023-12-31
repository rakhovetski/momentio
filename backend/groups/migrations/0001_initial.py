# Generated by Django 3.2.21 on 2023-10-04 09:06

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('hex_color', models.CharField(default='#4d10bd', max_length=7, null=True, validators=[django.core.validators.RegexValidator(re.compile('^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'), 'Enter a valid color')])),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_groups', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
                'ordering': ['title'],
            },
        ),
    ]
