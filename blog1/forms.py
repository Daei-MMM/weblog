from django import forms
from datetime import datetime


class CreateForms (forms.Form):
        title=forms.CharField()
        text=forms.CharField(widget=forms.Textarea())
      
class TodoForm(forms.Form):
        title=forms.CharField()
        text=forms.CharField(widget=forms.Textarea())
      

        
      

        
       
