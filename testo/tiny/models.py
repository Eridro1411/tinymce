from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class Testo(models.Model):
    titolo = models.CharField(max_length=100)
    area = HTMLField()
