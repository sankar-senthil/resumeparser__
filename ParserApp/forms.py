from unicodedata import name
from django import forms
from django.core.validators import FileExtensionValidator

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes',
        validators=[FileExtensionValidator(allowed_extensions=['pdf','docx'])]
    )

class Resumfield(forms.Form):
    CandidateName = forms.CharField(label='Candidate Name' )
    EmailID = forms.CharField(label='Email ID' )
    ContactNumber = forms.CharField(label='Contact Number')
    Location = forms.CharField(label='Location')
    KeySkills = forms.CharField(label='Key Skills')
    Experience = forms.CharField(label='Experience')
    designation = forms.CharField(label='Designation')
    Command = forms.CharField(label='Command')
    college_name = forms.CharField(label='College Name')
    company_names = forms.CharField(label='Company Name')
    total_exp = forms.CharField(label='Total Experience')
    


    