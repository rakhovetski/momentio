from django.contrib import admin
from django.contrib.auth.models import Group as DjangoGroup

from groups.models import Group, Tag
from post.models import Post


admin.site.unregister(DjangoGroup)


class PostInline(admin.TabularInline):
    model = Post
    extra = 1


class TagInline(admin.TabularInline):
    model = Group.tags.through
    extra = 1


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'hex_color']
    inlines = [TagInline, PostInline]


class GroupInline(admin.TabularInline):
    model = Group.tags.through
    extra = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title',]
    list_filter = ['title',]
    inlines = [GroupInline, ]