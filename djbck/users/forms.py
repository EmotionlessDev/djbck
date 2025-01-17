from django import forms
from random_username.generate import generate_username
from users.models import User


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput,
        required=True,
        max_length=100,
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        required=True,
        min_length=8,
        max_length=40,
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput,
        required=True,
        min_length=8,
        max_length=40,
    )

    def check_password(self):
        cd = self.cleaned_data
        password1 = cd['password1']
        password2 = cd['password2']

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if not user.username:
            user.username = generate_username(1)[0]
        user.is_active = True

        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ("email", )


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "username", "is_active", "is_staff"]
