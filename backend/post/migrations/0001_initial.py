# Generated by Django 3.2.21 on 2023-10-04 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=2000, null=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('slug', models.SlugField(max_length=100, null=True)),
                ('tags', models.CharField(choices=[('VG', 'Very Good'), ('GD', 'Good'), ('NL', 'Normal'), ('BD', 'Bad'), ('VB', 'Very Bad')], max_length=2)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='groups.group')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='PostPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_photos', to='post.post')),
            ],
            options={
                'verbose_name': 'post_photo',
                'verbose_name_plural': 'post_photos',
                'ordering': ['post'],
            },
        ),
    ]
