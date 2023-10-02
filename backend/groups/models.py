import re

from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify

from account.models import CustomUser


class Tag(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['title']

    def __str__(self) -> str:
        return self.title


color_re = re.compile('^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
validate_color = RegexValidator(color_re, 'Enter a valid color')


class Group(models.Model):
    title = models.CharField(max_length=100)
    hex_color = models.CharField(max_length=7, validators=[validate_color])
    slug = models.SlugField(max_length=100, unique=True)

    tag = models.ManyToManyField(Tag, related_name='groups')
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='user_groups')    

    
    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'
        ordering = ['title']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Group, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.slug}: {self.user}'
    
