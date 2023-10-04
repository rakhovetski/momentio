from django.contrib import admin
from django.contrib.auth.models import Group as DjangoGroup

from groups.models import Group
from post.models import Post


admin.site.unregister(DjangoGroup)


class PostInline(admin.TabularInline):
    model = Post
    extra = 1


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'hex_color']
    inlines = [PostInline, ]

