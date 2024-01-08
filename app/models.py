from django.db import models
# Create your models here.
class Application(models.Model):
    name=models.CharField(max_length=50, null=True, blank=True)
    email=models.EmailField(null=True,blank=True)
    education=models.CharField(max_length=100, null=True,blank=True)
    address=models.CharField(max_length=200,null=True,blank=True)
    certify=models.CharField(max_length=200,null=True,blank=True)
    file=models.FileField(null=True, blank=True)
    taxSoftware=models.CharField(max_length=200,null=True,blank=True)
    availability=models.CharField(max_length=200,null=True,blank=True)
    phone=models.CharField(max_length=200,null=True,blank=True)
    years=models.PositiveIntegerField(null=True,blank=True)
    workExperience=models.TextField(null=True,blank=True)
    def __str__(self):
        return str(self.name)
