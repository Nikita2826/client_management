from django import forms
from .models import Employee

ProjectDomain = [("SAAS","SAAS"),("Ecommerce","Ecommerce"),("CRM","CRM"),("ERP","ERP"),("Finance","Finance")]
Status = [("Onboarded","Onboarded"),("Not Onboarded","Not Onboarded")]
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

        widgets = {
            "status":forms.Select(choices=Status),
            "projectDomain":forms.Select(choices=ProjectDomain)
        }
