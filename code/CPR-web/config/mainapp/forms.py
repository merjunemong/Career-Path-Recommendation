# mainapp/forms.py
from django import forms
import json

class UploadFileForm(forms.Form):
    file = forms.FileField()
    
class JobForm(forms.Form):
    job = forms.CharField(label='직업', max_length=100)
    
class ListForm(forms.Form):
    skills = forms.CharField(label='Skills', widget=forms.HiddenInput)

    def clean_skills(self):
        data = self.cleaned_data['skills']
        return data