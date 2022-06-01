from django import forms 

class UserForm(forms.Form):
    Text=forms.CharField(widget=forms.Textarea())