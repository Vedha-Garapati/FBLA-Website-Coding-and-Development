from django.db import models
# Create your models here.
# Application Model: created a class called Application using the models provided by Django to initialize variables for each input field
class Application(models.Model):
    firstName=models.CharField(max_length=50, null=True, blank=True)#Initializes data variable for the name box, accepting a maximum length of 50 characters


    lastName=models.CharField(max_length=50, null=True, blank=True)

    position=models.CharField(max_length=75, null=True, blank=True)

    email=models.EmailField(null=True,blank=True)#Initializes data variable for the email box, designed specifically to receive email info

    phone=models.CharField(max_length=10,null=True,blank=True)#Initializes data variable for applicants phone number.Accepts a maximum of 10 characters.
    
    address=models.CharField(max_length=200,null=True,blank=True)

    city=models.CharField(max_length=65, null=True, blank=True)

    state=models.CharField(max_length=2, null=True, blank=True)

    zip=models.PositiveIntegerField(null=True, blank=True) 
    
    certifications=models.CharField(max_length=200,null=True,blank=True)#Initializes data variable for the applicants certifications. Accepts maximum of 200 characters

    taxKnowledge=models.TextField(null=True, blank=True)

    taxSoftware=models.CharField(max_length=200,null=True,blank=True)#Initializes data variable for the applicants tax software experience. Accepts maximum of 200 characters

    years=models.PositiveIntegerField(null=True,blank=True)#Initializes data variable for applicants years of experience.

    availability=models.CharField(max_length=200,null=True,blank=True)#Initializes data variable for the applicants availability during tax season input box. Accepts max 200 characters

    reference1Name=models.CharField(max_length=60, null=True, blank=True)

    reference1Relationship=models.CharField(max_length=60, null=True, blank=True)

    reference1Phone=models.CharField(max_length=10,null=True,blank=True)

    reference2Name=models.CharField(max_length=60, null=True, blank=True)

    reference2Relationship=models.CharField(max_length=60, null=True, blank=True)

    reference2Phone=models.CharField(max_length=10,null=True,blank=True)

    reasonForApplying=models.TextField(null=True,blank=True)

    recentStartDate=models.DateField(null=True, blank=True)

    recentEndDate=models.DateField(null=True, blank=True)

    recentJobTitle=models.CharField(max_length=100, null=True, blank=True)

    recentCompany=models.CharField(max_length=100, null=True, blank=True)

    recentCity=models.CharField(max_length=50, null=True, blank=True)

    recentState=models.CharField(max_length=2, null=True, blank=True)

    recentReasonForLeaving=models.CharField(max_length=350, null=True, blank=True)

    recentJobDescription=models.TextField(null=True, blank=True)

    extraInfo=models.TextField(null=True, blank=True)


    def __str__(self):
        return str(self.firstName)#This method returns the name of the class as the category for this data set. In this case, it will return 'Application' but django will change the name of the dataset to 'Applications' automatically.
