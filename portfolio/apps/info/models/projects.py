from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    summary = models.TextField(max_length=300)
    order = models.IntegerField(unique=True, )


class Thumbnail(models.Model):
    images = models.ImageField(upload_to="project/thumbnail")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, )
