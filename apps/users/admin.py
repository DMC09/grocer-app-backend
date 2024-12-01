from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Group, GroupMember, User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('avatar_url', 'phone', 'in_group', 'view_all', 'view_by_category')}),
    )

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'share_code', 'created_at')
    search_fields = ('name', 'share_code')

@admin.register(GroupMember)
class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'user', 'is_admin', 'confirmation_accepted')
    list_filter = ('is_admin', 'confirmation_accepted')
    search_fields = ('group__name', 'user__username') 