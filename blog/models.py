from email.policy import default
from django.db import models
from django.forms import FileField
from tinymce.models import HTMLField

# Create your models here.
class banner(models.Model):
    bannerheading = models.CharField(max_length=50)
    banner_image = models.FileField(upload_to= "media",max_length=250,null=False,default= None)


class blogs(models.Model):
    blog_date =models.CharField(max_length=50)
    blog_heading = models.TextField()
    blog_half = models.TextField( null = False, default=None)
    blog_description = HTMLField()
    blog_catagory = models.IntegerField(null= False,default=None)
    blog_image = models.FileField(upload_to ="media",max_length=250,null =False, default= None)



class catogry(models.Model):
    catogry_head = models.CharField(max_length=50) 
    catogry_value=models.CharField(max_length=20)  


        


