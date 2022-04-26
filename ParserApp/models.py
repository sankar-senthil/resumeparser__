from django.db import models

class Document(models.Model):
    docfile = models.FileField()


class Resum(models.Model):
    CandidateName = models.CharField(null=True, max_length = 250)
    EmailID = models.CharField(null=True, max_length = 250)
    ContactNumber = models.CharField(null=True, max_length = 250)
    Location = models.CharField(null=True, max_length = 250)
    KeySkills = models.CharField(null=True, max_length = 250)
    Experience = models.CharField(null=True, max_length = 250)
    designation = models.CharField(null=True, max_length = 250)
    Command = models.CharField(null=True, max_length = 250)
    college_name = models.CharField(null=True, max_length = 250)
    company_names = models.CharField(null=True, max_length = 250)
    total_exp= models.CharField(null=True, max_length = 250)