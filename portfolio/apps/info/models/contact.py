from django.contrib.auth import get_user_model
from django.db import models

from portfolio.apps.info.utils import phone_number_validator

User = get_user_model()


class SocialProfile(models.Model):
    linkedin = models.URLField("linkedin url")
    github = models.URLField("github url")
    stackoverflow = models.URLField("stackoverflow url")
    email = models.EmailField("email address")


class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    social = models.OneToOneField(SocialProfile, on_delete=models.RESTRICT)
    address = models.CharField("address", max_length=150)
    phone_number = models.CharField("phone number", max_length=14,validators=[phone_number_validator])
