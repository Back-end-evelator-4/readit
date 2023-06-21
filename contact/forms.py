from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your Name'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your Email'
        })
        self.fields['subject'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Subject'
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Message'
        })

    def clean(self):
        self.cleaned_data['name'] = self.cleaned_data['name'].title()
        self.cleaned_data['subject'] = self.cleaned_data['subject'].capitalize()
        self.cleaned_data['message'] = self.cleaned_data['message'].capitalize()
