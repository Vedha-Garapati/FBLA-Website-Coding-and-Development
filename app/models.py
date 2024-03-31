from django.db import models
# Create your models here.
# Application Model: created a class called Application using the models provided by Django to initialize variables for each input field

class Application(models.Model):
    name=models.CharField(max_length=50, null=True, blank=True)#Initializes data variable for the name box, accepting a maximum length of 50 characters

    email=models.EmailField(null=True,blank=True)#Initializes data variable for the email box, designed specifically to receive email info

    education=models.CharField(max_length=100, null=True,blank=True)#Initializes data variable for the highest education level input box. Accepts maximum of 100 characters
    
    address=models.CharField(max_length=200,null=True,blank=True)#Initializes data variable for the applicants address. Accepts maximum of 200 characters

    certify=models.CharField(max_length=200,null=True,blank=True)#Initializes data variable for the applicants certifications. Accepts maximum of 200 characters

    middle=models.CharField(max_length=1,null=True,blank=True)

    taxSoftware=models.CharField(max_length=200,null=True,blank=True)#Initializes data variable for the applicants tax software experience. Accepts maximum of 200 characters

    availability=models.CharField(max_length=200,null=True,blank=True)#Initializes data variable for the applicants availability during tax season input box. Accepts max 200 characters

    phone=models.CharField(max_length=10,null=True,blank=True)#Initializes data variable for applicants phone number.Accepts a maximum of 10 characters.

    years=models.PositiveIntegerField(null=True,blank=True)#Initializes data variable for applicants years of experience.

    workExperience=models.TextField(null=True,blank=True)#Initializes data variable for applicants work experience. This is a text field as it is expected that the client go more in depth in this input box.

    def __str__(self):
        return str(self.name)#This method returns the name of the class as the category for this data set. In this case, it will return 'Application' but django will change the name of the dataset to 'Applications' automatically.
