from django.contrib.auth import get_user_model
from django.db import models
from PIL import Image

from portfolio.core.constant import ICON_SIZE
from portfolio.utils.image import resize_image, renamed_image_loc

User = get_user_model()

class Technology(models.Model):
    name = models.CharField("technology name",max_length=100)
    icon = models.ImageField(upload_to=renamed_image_loc, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # saving image first

        resize_image(self.icon, height=ICON_SIZE, width=ICON_SIZE)

    def __str__(self):
        return "%s : %s" %(self.__class__.__name__, self.name)


class SkillType(models.Model):
    name = models.CharField(max_length=150, )

    def __str__(self):
        return "%s : %s" %(self.__class__.__name__, self.name)


class Skill(models.Model):
    class LevelChoice(models.TextChoices):
        BEGINNER = 'BEGNR', 'Beginner',
        INTERMEDIATE = 'INTRM', 'Intermediate',
        EXPERT = 'EXPRT', 'Expert'

    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    skill_type = models.ForeignKey(SkillType, on_delete=models.CASCADE)
    level = models.CharField(max_length=5, choices=LevelChoice.choices,
                             default=LevelChoice.INTERMEDIATE)


