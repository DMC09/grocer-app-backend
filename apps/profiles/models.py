from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    avatar_url = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    in_group = models.BooleanField(null=True, default=False)
    select_id = models.CharField(max_length=255, null=True, blank=True)
    view_all = models.BooleanField(default=True)
    view_by_category = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Group(models.Model):
    name = models.CharField(max_length=255, null=True)
    image = models.URLField(null=True, blank=True)
    share_code = models.CharField(max_length=50, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name or 'Unnamed Group'

class GroupMember(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='members')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    confirmation_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = ['group', 'profile']

    def __str__(self):
        return f"{self.profile} in {self.group}" 