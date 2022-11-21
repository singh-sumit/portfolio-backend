from django.db import models
from django.contrib.auth import get_user_model

from portfolio.apps.info.models.skill import Skill

User = get_user_model()


class Company(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=150)
    major_task = models.TextField()
    skills = models.ManyToManyField(Skill, )

    joined_date = models.DateField()
    end_date = models.DateField(blank=True,)
