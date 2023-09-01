from django.db.models import fields
from django import forms
from core.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            "name",
            "email",
            "subject",
            "message",
        )

        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Name",
                "class": "form-group"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Email",
                "class": "form-group"
            }),
            "subject": forms.TextInput(attrs={
                "placeholder": "Subject",
                "class": "form-group"
            }),
            "message": forms.Textarea(attrs={
                "placeholder": "message",
                "class": "form-group",
                "rows": 5
            })
        }

    def clean_message(self):
        if " " not in self.cleaned_data.get("message"):
            self.add_error("message", "Message is null")
        
        return self.cleaned_data.get("message")


        

