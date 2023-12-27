from django.shortcuts import render
from django.http import HttpResponse
from .models import Apply
from app.functions import handle_uploaded_file  
# Create your views here.
def index(request):
    if request.method=="POST":
        apply = Apply()
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
        clientInteraction=request.POST.get('clientInteraction')
        legislationKnowledge=request.POST.get('legislationKnowledge')
        teamwork=request.POST.get('teamwork')
        problemSolving=request.POST.get('problemSolving')
        professionalDevelopment=request.POST.get('professionalDevelopment')
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
        apply.clientInteraction=clientInteraction
        apply.legislationKnowledge=legislationKnowledge
        apply.teamwork=teamwork
        apply.problemSolving=problemSolving
        apply.professionalDevelopment=professionalDevelopment
        apply.save()
        return HttpResponse("<h1>Thank You For Applying</h1>")

    return render(request, 'index.html')