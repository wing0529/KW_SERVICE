from django.db import models

# Create your models here.
class mymodel(models.Model):
    title = models.TextField()
    content = models.TextField()
    user = models.TextField()