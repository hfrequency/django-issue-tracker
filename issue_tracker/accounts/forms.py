from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import Input
import logging
import settings

log = logging.getLogger("app." + __name__)

class EmailInput(Input):
    input_type = 'email'

class UserCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=75,
        widget=forms.TextInput(attrs={'placeholder': 'user name'}),
        error_messages={'required': 'Please provide a user name',
                        'invalid': 'Please enter a valid name'})

    email = forms.EmailField(max_length=75, required=True,
        widget=EmailInput(attrs={'placeholder':'Required'}),
        error_messages={'invalid': 'Please enter a valid email address',
                        'required': 'Please provide your email address'})

    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm = forms.CharField(label="Confirm Password", widget=forms.PasswordInput,
        help_text = "Enter password again for verification.")

    class Meta:
        model = User
        fields = ("username", "email", "password", "confirm")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise forms.ValidationError("A user with this email address already exists.")

    def clean_confirm(self):
        password = self.cleaned_data.get("password", "")
        confirm = self.cleaned_data["confirm"]
        if password != confirm:
            raise forms.ValidationError("The password fields didn't match.")

        return confirm

    def clean_email(self):
        """
        Make sure the email address is unique.
        """
        email = self.cleaned_data["email"]
        if not email:
            return email
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError("This email address is already in use.")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.email = user.username
            user.save()
        return user
