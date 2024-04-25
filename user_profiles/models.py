from enum import Enum

from django.contrib.auth.models import User
from django.db import models

from bitrix24_integration.models import Contact


class RoleEnum(Enum):
    CUSTOMER = 'customer'
    PERFORMER = 'performer'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='user_profiles')
    role = models.CharField(max_length=20, choices=[(role.value, role.value) for role in RoleEnum])
    contact_info = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
