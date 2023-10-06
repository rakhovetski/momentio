# Generated by Django 3.2.21 on 2023-10-06 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, choices=[('VG', 'Very Good'), ('GD', 'Good'), ('NL', 'Normal'), ('BD', 'Bad'), ('VB', 'Very Bad')], max_length=2),
        ),
    ]