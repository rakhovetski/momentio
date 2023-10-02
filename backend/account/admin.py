from django.contrib import admin

from account.models import CustomUser
from groups.models import Group


class GroupInline(admin.TabularInline):
    model = Group
    extra = 1


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'email']
    ordering = ['email', ]
    search_fields = ['email', ]
    inlines = [GroupInline, ]
