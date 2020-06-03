from django import forms
from .models import Emp


class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = ['Emp_ID', 'First_Name', 'Last_Name', 'Email', 'Phone', 'Job_Title',
                  'Department', 'Address', 'City', 'Zipcode', 'Country', 'Salary']
