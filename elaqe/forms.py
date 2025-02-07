from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'phone', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ad və Soyadınızı daxil edin'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-poçtunuzu daxil edin'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon nömrənizi daxil edin'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mesajınızı daxil edin', 'rows': 4}),
        }
