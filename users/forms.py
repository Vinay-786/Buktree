from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "first_name",
                  "last_name", "password1", "password2")


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("bio", "profile_img", "email", "first_name", "last_name")
