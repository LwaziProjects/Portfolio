from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """Form for contact page"""

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "subject", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your Name",
                    "required": True,
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your Email",
                    "required": True,
                }
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your Phone (optional)"}
            ),
            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Subject",
                    "required": True,
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your Message",
                    "rows": 5,
                    "required": True,
                }
            ),
        }
