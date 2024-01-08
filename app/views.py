from django.shortcuts import render
from django.http import HttpResponse
from .models import Application
from app.functions import handle_uploaded_file  
# Create your views here.
def index(request):
    if request.method=="POST":
        apply = Application()
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        education=request.POST.get('education')
        certify=request.POST.get('certify')
        taxSoftware=request.POST.get('taxSoftware')
        file=request.POST.get('file')
        availability=request.POST.get('availability')
        phone=request.POST.get('phone')
        years=request.POST.get('years')
        workExperience=request.POST.get('workExperience')
        apply.name=name
        apply.email=email
        apply.address=address
        apply.education=education
        apply.certify=certify
        apply.taxSoftware=taxSoftware
        apply.file=file
        apply.availability=availability
        apply.phone=phone
        apply.years=years
        apply.workExperience=workExperience
        apply.save()
        return render(request, 'thank_you.html')


    return render(request, 'index.html')