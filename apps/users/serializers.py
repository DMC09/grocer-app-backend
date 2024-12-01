from rest_framework import serializers

from .models import Group, GroupMember, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'avatar_url', 'phone', 'in_group', 'select_id', 'view_all', 'view_by_category']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'image', 'share_code', 'created_at', 'modified_at']

class GroupMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMember
        fields = ['id', 'group', 'user', 'is_admin', 'confirmation_accepted', 'created_at', 'modified_at'] 