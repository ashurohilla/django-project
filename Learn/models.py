from django.db import models
from django.db import models
from django.forms import FileField
from tinymce.models import HTMLField

class learn(models.Model):
    Learn_Head =models.CharField(max_length=50)
    Learn_heading = models.TextField()
    Learn_description = HTMLField()
    


# Create your models here.
