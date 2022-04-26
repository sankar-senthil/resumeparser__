from django.shortcuts import render, redirect
from .models import Document, Resum
from .forms import DocumentForm, Resumfield
from pyresparser import ResumeParser
from django.conf import settings
import os

# Create your views here.

def home(requests):
    docform = DocumentForm()
    dataform = Resumfield()
    content = {"docform":docform}
    print(requests.POST)    
    if requests.method == 'POST':
        form = DocumentForm(requests.POST, requests.FILES)
        if form.is_valid():
            newdoc = Document(docfile = requests.FILES['docfile'])
            filename = str(requests.FILES['docfile']).replace(' ','')
            aps_path = f"{settings.MEDIA_ROOT}/{filename}"
            if aps_path:
                try:
                    os.remove(aps_path)
                except:pass
            else:pass
            newdoc.save()
            data = {}
            resdata = ResumeParser(aps_path).get_extracted_data()
            content = {"dataform":dataform,"resdata":resdata}
            print("------------------------------------")
            return render(requests,"resumepraser/resumefield.html",content)

        else:
            datains = Resum()
            datains.CandidateName = requests.POST.get('CandidateName')
            datains.EmailID = requests.POST.get('EmailID')
            datains.ContactNumber = requests.POST.get('ContactNumber')
            datains.Location = requests.POST.get('Location')
            datains.KeySkills = requests.POST.get('KeySkills')
            datains.Experience = requests.POST.get('Experience')
            datains.designation = requests.POST.get('designation')
            datains.Command = requests.POST.get('Command')
            datains.college_name = requests.POST.get('college_name')
            datains.company_names = requests.POST.get('company_names')
            datains.total_exp = requests.POST.get('total_exp')
            datains.save()

               

    return render(requests,'resumepraser/home.html', content)

def resume_field(requests):
    return render(requests,'resumepraser/resumefield.html')
