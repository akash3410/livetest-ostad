from django import forms
from .models import Contact

class AddContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        }
        
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']