from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *


class UserForm(UserCreationForm):
    class Meta:
        model = Faculty
        fields = ('username', 'first_name', 'last_name', 'password')


class EditProfileForm(UserChangeForm):
    class Meta:
        model = Faculty
        fields = ('username', 'first_name', 'last_name', 'subject')


"""class EditStudentProfileForm(UserChangeForm):
    

    class Meta:
        model = Student
        fields = ('phone_number', 'qualification', 'current_city', 'photo', 'resume', 'address')"""
