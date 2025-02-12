from django import forms
import re

class PdfForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter full name'}),
        error_messages={'required': 'Name is required'}
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter email'}),
        error_messages={'invalid': 'Enter a valid email address'}
    )

    phone = forms.CharField(
        max_length=10,
        min_length=10,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter 10-digit phone number'}),
        error_messages={'required': 'Phone number is required'}
    )

    address = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter your full address', 'rows': 2}),
        required=True
    )

    city = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter city'}),
    )

    state = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter state'}),
    )

    country = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter country'}),
    )

    zip_code = forms.CharField(
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter ZIP code'}),
        error_messages={'required': 'ZIP code is required'}
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Provide a short description', 'rows': 3}),
        required=True,
        min_length=10,
        error_messages={'required': 'Description is required', 'min_length': 'Minimum 10 characters required'}
    )

    additional_info = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Additional Information (optional)', 'rows': 3}),
        required=False
    )

    def clean_name(self):
        """Ensure name contains only alphabets"""
        name = self.cleaned_data['name']
        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError("Name should contain only letters")
        return name

    def clean_phone(self):
        """Ensure phone number contains only digits and is exactly 10 digits"""
        phone = self.cleaned_data['phone']
        if not re.match(r'^\d{10}$', phone):
            raise forms.ValidationError("Enter a valid 10-digit phone number")
        return phone


