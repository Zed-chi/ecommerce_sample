from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"})
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    def clean(self):
        data = self.cleaned_data
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("pass match")
        return data

    def clean_username(self):
        username = self.cleaned_data.get("username")
        queryset = User.objects.get(username=username)
        if queryset:
            raise ValidationError("name exists")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        queryset = User.objects.get(email=email)
        if queryset:
            raise ValidationError("email exists")
