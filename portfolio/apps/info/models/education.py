from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Institution(models.Model):
    class UniversityBoardChoice(models.TextChoices):
        SLC = 'slc', 'SLC'
        HSEB = 'hseb', 'HSEB'
        PURWANCHAL_UNIVERSITY = 'PU', 'Purwanchal University'

    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    university_board = models.CharField(max_length=4, choices=UniversityBoardChoice.choices,
                                        default=UniversityBoardChoice.PURWANCHAL_UNIVERSITY)

    def __str__(self):
        return f"{self.__class__.__name__} : {self.name}"

class Education(models.Model):
    class LevelChoice(models.TextChoices):
        PLUSTWO = 'PO', '+2'
        BACHELOR = 'BR', 'Bachelor'
        MASTER = 'MR', 'Master'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT)
    level = models.CharField(max_length=2, choices=LevelChoice.choices,
                             default=LevelChoice.PLUSTWO)
    enroll_faculty = models.CharField(max_length=150)

    start_date = models.DateField("start date", auto_now_add=True)
    end_date = models.DateField("end date", blank=True)

    def __str__(self):
        return f"{self.user} : {self.institution}"


