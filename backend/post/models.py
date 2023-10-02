from django.db import models
from django.utils.text import slugify

from groups.models import Group


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    slug = models.SlugField(max_length=100, null=True)

    group = models.ForeignKey(Group, on_delete=models.PROTECT, related_name='posts', null=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['title']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.slug}: ({self.latitude}, {self.longitude})'


class PostPhoto(models.Model):
    post = models.ForeignKey(Post, related_name='post_photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')

    class Meta:
        verbose_name = 'post_photo'
        verbose_name_plural = 'post_photos'
        ordering = ['post']

    def __str__(self) -> str:
        return f'Image: {self.post}'