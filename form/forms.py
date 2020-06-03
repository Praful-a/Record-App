from django import forms
from .models import Emp


class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = ['Emp_ID', 'First_Name', 'Last_Name', 'Email', 'Phone', 'Job_Title',
                  'Department', 'Address', 'City', 'Zipcode', 'Country', 'Salary']


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = ['Emp_ID', 'First_Name', 'Last_Name', 'Email', 'Phone', 'Job_Title',
                  'Department', 'Address', 'City', 'Zipcode', 'Country', 'Salary']

        def save(self, commit=True):
            data = self.instance
            data.Emp_ID = self.cleaned_data['Emp_ID']

            if commit:
                data.save()
            return data
