from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    tehnology = models.CharField(max_length=30)
    image = models.FileField(upload_to='img/')