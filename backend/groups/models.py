import re

from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify

from account.models import CustomUser


color_re = re.compile('^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
validate_color = RegexValidator(color_re, 'Enter a valid color')


class Group(models.Model):
    title = models.CharField(max_length=100)
    hex_color = models.CharField(max_length=7, validators=[validate_color], null=True, default='#4d10bd')
    slug = models.SlugField(max_length=100, unique=True, null=True)

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
    
