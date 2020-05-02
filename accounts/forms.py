from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from accounts.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=60, help_text='Required. Add a valid email address'
    )

    class Meta:
        model = Account
        fields = ("email", "username", "password1", "password2")


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid:
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login!")


class AccountsUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'username', 'profile_pic', 'name',
                  'work_line', 'skills', 'profession', 'phone',)

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(
                    pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise form.ValidationError(
                'Email "%s" is already in use.' % email
            )

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(
                    username=username
                )
            except Account.DoesNotExist:
                return username
            raise form.ValidationError(
                'Username "%s" is already in use.' % username
            )

    def clean_basic(self):
        if self.is_valid():
            profile_pic = self.cleaned_data['profile_pic']
            name = self.cleaned_data['name']
            work_line = self.cleaned_data['work_line']
            skills = self.cleaned_data['skills']
            profession = self.cleaned_data['profession']
            phone = self.cleaned_data['phone']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(
                    profile_pic=profile_pic,
                    name=name,
                    work_line=work_line,
                    skills=skills,
                    profession=profession,
                    phone=phone
                )
            except Account.DoesNotExist:
                return profile_pic
            raise form.ValidationError(
                'UserImage "%s" already exists.' % profile_pic
            )
