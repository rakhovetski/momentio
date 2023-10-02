from django.contrib import admin

from post.models import Post, PostPhoto


class PostPhotoInline(admin.TabularInline):
    model = PostPhoto
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'latitude', 'longitude']
    search_fields = ['title', ]
    inlines = [PostPhotoInline, ]
