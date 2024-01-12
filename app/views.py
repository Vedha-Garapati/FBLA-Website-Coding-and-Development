#Import statement allows django to render HTML pages
from django.shortcuts import render

#Import statement allows django to return a physical response in the HTML page
from django.http import HttpResponse

#Import statement allows this file to access the 'Application' class in which all the data types for the job application have been initialized.
from .models import Application

# Create your views here.
from app.functions import handle_uploaded_file  
#Primary method is commonly reffered to as the 'index' method and the 'request' parameter refers to where the method will be grabbing data from.
def index(request):
    #Runs a condition asking if the data was written by a user, or 'POST' data, run the following code beneath.
    if request.method=="POST":
        
        #Creates a constructor using the application class
        apply = Application()

        #Grabs the user input data from the input box that has the name of 'name' on it and stores it in this variable
        name=request.POST.get('name')

        #Grabs the user input data from the input box that has the name of 'email' on it and stores it in this variable
        email=request.POST.get('email')

        #Grabs the user input data from the input box that has the name of 'address' on it and stores it in this variable
        address=request.POST.get('address')

        #Grabs the user input data from the input box that has the name of 'education' on it and stores it in this variable
        education=request.POST.get('education')

        #Grabs the user input data from the input box that has the name of 'certify' on it and stores it in this variable
        certify=request.POST.get('certify')

        #Grabs the user input data from the input box that has the name of 'taxSoftware' on it and stores it in this variable
        taxSoftware=request.POST.get('taxSoftware')

        #Grabs the user input data from the input box that has the name of 'file' on it and stores it in this variable
        file=request.POST.get('file')

        #Grabs the user input data from the input box that has the name of 'availability' on it and stores it in this variable
        availability=request.POST.get('availability')

        #Grabs the user input data from the input box that has the name of 'phone' on it and stores it in this variable
        phone=request.POST.get('phone')

        #Grabs the user input data from the input box that has the name of 'years' on it and stores it in this variable
        years=request.POST.get('years')

        #Grabs the user input data from the input box that has the name of 'workExperience' on it and stores it in this variable
        workExperience=request.POST.get('workExperience')

        #Stores the variable we initalized earlier in this code segement and stores it in the 'name' section of the Application dataset
        apply.name=name

        #Stores the variable we initalized earlier in this code segement and stores it in the 'email' section of the Application dataset
        apply.email=email

        #Stores the variable we initalized earlier in this code segement and stores it in the 'address' section of the Application dataset
        apply.address=address

        #Stores the variable we initalized earlier in this code segement and stores it in the 'education' section of the Application dataset
        apply.education=education

        #Stores the variable we initalized earlier in this code segement and stores it in the 'certify' section of the Application dataset
        apply.certify=certify

        #Stores the variable we initalized earlier in this code segement and stores it in the 'taxSoftware' section of the Application dataset
        apply.taxSoftware=taxSoftware

        #Stores the variable we initalized earlier in this code segement and stores it in the 'file' section of the Application dataset
        apply.file=file

        #Stores the variable we initalized earlier in this code segement and stores it in the 'availability' section of the Application dataset
        apply.availability=availability

        #Stores the variable we initalized earlier in this code segement and stores it in the 'phone' section of the Application dataset
        apply.phone=phone

        #Stores the variable we initalized earlier in this code segement and stores it in the 'years' section of the Application dataset
        apply.years=years

        #Stores the variable we initalized earlier in this code segement and stores it in the 'workExperience' section of the Application dataset
        apply.workExperience=workExperience

        #Saves the current version of the application class in the admin database 
        apply.save()

        #If everything went well and all the data was saved, the program will take you to the thank you page
        return render(request, 'thank_you.html')
        

    #Will always keep this page operating whether or not the application data was grabbed successfully.
    return render(request, 'index.html')

def application(request):
    return render(request, 'app.html')

def applyHere(request):
    return render(request, 'work.html')