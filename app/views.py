#Import statement allows django to render HTML pages
from django.shortcuts import render

#Import statement allows django to return a physical response in the HTML page
from django.http import HttpResponse

#Import statement allows this file to access the 'Application' class in which all the data types for the job application have been initialized.
from .models import Application

# Create your views here.
from app.functions import handle_uploaded_file  
#Primary method is commonly reffered to as the 'index' method and the 'request' parameter refers to where the method will be grabbing data from.
def main(request):
    return render(request,'index.html')
def index(request):
    #Runs a condition asking if the data was written by a user, or 'POST' data, run the following code beneath.
    if request.method=="POST":
        
        #Creates a constructor using the application class
        apply = Application()

        #Grabs the user input data from the input box that has the name of 'name' on it and stores it in this variable
        firstName=request.POST.get('firstName')

        #Stores the variable we initalized earlier in this code segement and stores it in the 'name' section of the Application dataset
        apply.firstName=firstName

        lastName=request.POST.get('lastName')

        apply.lastName=lastName

        position=request.POST.get('position')

        apply.position=position

        address=request.POST.get('address')

        apply.address=address

        city=request.POST.get('city')

        apply.city=city

        state=request.POST.get('state')

        apply.state=state

        zip=request.POST.get('zip')

        apply.zip=zip

        phone=request.POST.get('phone')

        apply.phone=phone

        email=request.POST.get('email')

        apply.email=email

        reference1Name=request.POST.get('reference1Name')

        apply.reference1Name=reference1Name

        reference1Relationship=request.POST.get('reference1Relationship')

        apply.reference1Relationship=reference1Relationship

        reference1Phone=request.POST.get('reference1Phone')

        apply.reference1Phone=reference1Phone

        reference2Name=request.POST.get('reference2Name')

        apply.reference2Name=reference2Name

        reference2Relationship=request.POST.get('reference2Relationship')

        apply.reference2Relationship=reference2Relationship

        reference2Phone=request.POST.get('reference2Phone')

        apply.reference2Phone=reference2Phone

        reasonForApplying=request.POST.get('reasonForApplying')

        apply.reasonForApplying=reasonForApplying

        years=request.POST.get('years')

        apply.years=years

        certifications=request.POST.get('certifications')

        apply.certifications=certifications

        availability=request.POST.get('availability')

        apply.availability=availability

        taxKnowledge=request.POST.get('taxKnowledge')

        apply.taxKnowledge=taxKnowledge

        taxSoftware=request.POST.get('taxSoftware')

        apply.taxSoftware=taxSoftware

        recentStartDate=request.POST.get('recentStartDate')

        apply.recentStartDate=recentStartDate

        recentEndDate=request.POST.get('recentEndDate')

        apply.recentEndDate=recentEndDate

        recentJobTitle=request.POST.get('recentJobTitle')

        apply.recentJobTitle=recentJobTitle

        recentCompany=request.POST.get('recentCompany')

        apply.recentCompany=recentCompany

        recentCity=request.POST.get('recentCity')

        apply.recentCity=recentCity

        recentState=request.POST.get('recentState')

        apply.recentState=recentState

        recentReasonForLeaving=request.POST.get('recentReasonForLeaving')

        apply.recentReasonForLeaving=recentReasonForLeaving

        recentJobDescription=request.POST.get('recentJobDescription')

        apply.recentJobDescription=recentJobDescription

        extraInfo=request.POST.get('extraInfo')

        apply.extraInfo=extraInfo



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

def AI(request):
    return render(request, 'AI.html')

def services(request):
    return render(request, 'services.html')